import random
import numpy as np

# Explanation is written at the end. 

WIDTH = 5
HEIGHT = 5
NUM_STATES = WIDTH * HEIGHT
TERMINAL_STATES = [WIDTH * HEIGHT - 1]
TOP_ROW = list(range(0,WIDTH))
BOTTOM_ROW = list(range(WIDTH*HEIGHT-WIDTH-1,WIDTH*HEIGHT))
LEFT_COLUMN = list(range(0, WIDTH * HEIGHT, WIDTH))
RIGHT_COLUMN = list(range(WIDTH - 1, WIDTH * HEIGHT, WIDTH))
ACTIONS = [-1, 1, -1 * HEIGHT, HEIGHT] # left, right, up, down
action_dict = {-1: 'left', 1: 'right', -1 * HEIGHT: 'up', HEIGHT: 'down'}
DISCOUNT = 0.9

def nextState(state, action):

    if (state in TOP_ROW) and (action == ACTIONS[2]):       # updated for top row
        return state, -1
    if (state in BOTTOM_ROW) and (action == ACTIONS[3]):    # updated for bottom row
        return state, -1 
    if (state in LEFT_COLUMN) and (action == ACTIONS[0]):
        return state, -1
    if (state in RIGHT_COLUMN) and (action == ACTIONS[1]):
        return state, -1
    next_state = state + action
    if next_state < 0 or next_state >= NUM_STATES:
        return state, -1
    if next_state in TERMINAL_STATES:
        return -1, 20                                     # Reward is only at terminal state.
    return next_state, 0

def startingState():
    state = random.choice(range(NUM_STATES))
    if state not in TERMINAL_STATES:
        return state
    else:
        while state in TERMINAL_STATES:
            state = random.choice(range(NUM_STATES))
    return state

def runEpisode(state, policy):
    episode = [state]
    episodeReward = [0]
    ep_length = 0
    while (ep_length < 90):
        action = random.choice(policy[state])
        next_state, reward = nextState(state, action)

        if next_state == -1:
            return episode, episodeReward
        
        else:
            episode.append(next_state)
            episodeReward.append(reward)

        state = next_state
        ep_length += 1
    return episode, episodeReward


def Policy_Improvement(OVF):    # Optimal Value function
    policy = []
    for i in range(HEIGHT):   
        for j in range(WIDTH):
            pol = []       # values for policy
            temp = {}      # dictionary saving the Value function values as keys, and has value list containing actions.
            for action in ACTIONS:
                next_state, reward = nextState(WIDTH*i+j, action)
                # print(next_i, next_j)
                a = (reward + DISCOUNT * OVF[next_state])
                pol.append(a)
                if a not in temp:
                    temp[a] = [action]                                  # python list containing np array type.
                else:
                    temp[a].append(action)
            policy.append(temp[np.max(pol)])
    print()
    print("                ********************* Policy: ********************")
    print()

    policy_case = [0 for _ in range(NUM_STATES)]
    for i in range(len(policy)):
        # print(policy[i])
        policy_case[i] = []
        for j in range(len(policy[i])):

            if policy[i][j] == -1 * HEIGHT:
                policy_case[i].append("up")
            elif policy[i][j] == HEIGHT:
                policy_case[i].append("down")
            elif policy[i][j] == -1:
                policy_case[i].append("left")
            elif policy[i][j] == 1:
                policy_case[i].append("right")

        if (i%5 == 4):        
            print(policy_case[i])
        else:
            print(policy_case[i], end = ',')
    return policy

def Policy_Iteration():     
    it = 0
    # Policy = [ACTIONS for _ in range(NUM_STATES)]
    Policy = [[random.choice(ACTIONS)] for _ in range(NUM_STATES)]
    # grid = np.zeros(HEIGHT * WIDTH)         # V(s)
    grid = np.full(HEIGHT * WIDTH, -10)         # V(s)
    grid[-1] = 0
    gridCounts = np.zeros(HEIGHT * WIDTH)   # N(s) main. 
    avgCounts = np.zeros(HEIGHT * WIDTH)    # Returns(s)

    policy_stable = False
    while (policy_stable == False):
        generated_episodes = 0
        while True:
            # keep iteration until convergence
            new_value = np.copy(grid)      # V'(s)
            state = startingState()
            e, eR = runEpisode(state, Policy)
            # print("length of episode: ", len(e))
            Ns_check = np.zeros(HEIGHT * WIDTH)   # N(s)_for temp_of_first_visit_Record
            avr = 0
            for i in range(len(e)):           # For Each episode
                if Ns_check[e[i]] == 0:       # For first-visit MC
                    Ns_check[e[i]] = 1        # updated only once in each episode
                    gridCounts[e[i]] += 1     # main update in N(s)
                    for j in range(len(e)-i):
                        avr +=  (DISCOUNT**j)*eR[j+i]
                    avgCounts[e[i]] = avr
                    new_value[e[i]] = grid[e[i]] + (1/(gridCounts[e[i]] + 1))*(avgCounts[e[i]] - grid[e[i]])
                                    
                    # V_new(s) = V_old(s) + (\frac{1}{N(s)+1})*(Returns(s) - V_old(s))
            generated_episodes += 1
            if np.sum(np.abs(grid - new_value)) < 1e-2:
                break
            grid = new_value
            # print("Najeeb")

        it += 1
        # input("Press Enter to continue...")
        print()
        # print("N(S): ", gridCounts)
        print("episodes generated for convergence in one evaluation : ", generated_episodes)
        print()
        np.set_printoptions(precision=2)
        print("      Value Function ")
        print()
        print(grid.reshape((WIDTH, HEIGHT)))
        print()
        new_policy = Policy_Improvement(grid)
        # print("New POlicy: ", new_policy)
        if Policy == new_policy:
            # print("HUrrha")
            policy_stable = True
        else: 
            # print("hurrah")
            Policy = new_policy 
        print()
    print("Converges in {} iterations".format(it))
    return grid
    
if __name__ == '__main__':
    Policy_Iteration()

'''
Explanation:
1. First we initialize uniform policy OR random initialize (I tried using both ways)
2. Value function is initialized with -1 for all state, only terminal state is set 0 
    so as to not get diverted and more focused towards terminal state
3. Using monte carlo for episode generation using current policy
4. Reward +10 is only at Terminal state, all actions to other states are set of reward -1. 

Problems & Reason :
    1. Infinite non ending episode:
            This was happening because after the first policy improvement, if there is a policy get generated
            and have no direction towards terminal state, the episode generation will stuck in an infinite loop.
            For this I fixed the episode length, but if it doesn't end to terminal still I will consider the episode and return.
            The reason becasue if I terminate and start generating an other episode, the same thing will happend as the policy 
            hasn't update and is same this time too. 

    2.  Update in convergence not happening significantly:
            In the second evaluation step, after first policy improvement, there isn't any significant improvement in value
            function observed. The reason behind must be after the first policy improvemnt, Monte Carlo is generating the other
            episode using the same improved policy. So the values must be the same on average, thats why no significant change is observed.

Findings:

On setting up the -1 as initial values of Value function, atleast half of the states started giving good results.
 
The one mitigation that I found that using Monte Carlo Search Tree method, this greedy appproach for taking action can resolved
but that is computationally too expensive and wasn't asked to do.  

'''
