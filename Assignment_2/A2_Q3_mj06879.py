import random
import numpy as np

WIDTH = 5
HEIGHT = 5
NUM_STATES = WIDTH * HEIGHT
TERMINAL_STATES = [WIDTH * HEIGHT - 1]
LEFT_COLUMN = list(range(0, WIDTH * HEIGHT, WIDTH))
RIGHT_COLUMN = list(range(WIDTH - 1, WIDTH * HEIGHT, WIDTH))
ACTIONS = [-1, 1, -1 * HEIGHT, HEIGHT] # left, right, up, down
action_dict = {-1: 'left', 1: 'right', -1 * HEIGHT: 'up', HEIGHT: 'down'}
DISCOUNT = 0.9

def nextState(state, action):
    if state == 1:
        return 21, 10
    if state == 3:
        return 13, 5
    if (state in LEFT_COLUMN) and (action == ACTIONS[0]):
        return state, -1
    if (state in RIGHT_COLUMN) and (action == ACTIONS[1]):
        return state, -1
    next_state = state + action
    if next_state < 0 or next_state >= NUM_STATES:
        return state, -1
    if next_state in TERMINAL_STATES:
        return -1, 0
    return next_state, 0

def startingState():
    state = random.choice(range(NUM_STATES))
    if state not in TERMINAL_STATES:
        return state
    else:
        while state in TERMINAL_STATES:
            state = random.choice(range(NUM_STATES))
    return state

def runEpisode(state):
    episode = [state]
    episodeReward = [0]
    while True:
        action = random.choice(ACTIONS)
        next_state, reward = nextState(state, action)

        if next_state == -1:
            return episode, episodeReward
        else:
            episode.append(next_state)
            episodeReward.append(reward)
        state = next_state

# UP = [-1, 0]
# DOWN = [1, 0]
# LEFT = [0, -1]
# RIGHT = [0, 1]

def Optimal_Policy(OVF):    # Optimal Value function
    policy = []
    for i in range(WIDTH):
        for j in range(HEIGHT):
            pol = []
            temp = {}
            for action in ACTIONS:
                next_state, reward = nextState(WIDTH*i + j, action)
                a = reward + DISCOUNT * OVF[next_state]
                # a = OVF[next_i, next_j]
                pol.append(a)
                if a not in temp:
                    temp[a] = [action]
                else:
                    temp[a].append(action)
            policy.append(temp[np.max(pol)])
    print()
    print("                ********************* Optimal Policy: ********************")
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

def Optimal_Value_function():      # upgraded figure_3_2()
    it = 0
    grid = np.zeros(HEIGHT * WIDTH)         # V(s)
    gridCounts = np.zeros(HEIGHT * WIDTH)   # N(s)
    avgCounts = np.zeros(HEIGHT * WIDTH)    # Returns(s)

    while True:
        # keep iteration until convergence
        new_value = np.copy(grid)      # V'(s)
        state = startingState()
        e, eR = runEpisode(state)
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
        if np.sum(np.abs(new_value - grid)) < 1e-2:
            break
        grid = new_value
        it += 1
        # input("Press Enter to continue...")
        np.set_printoptions(precision=2)
        print(grid)
        print()
    print("Converges in {} iterations".format(it))
    return grid
    # return grid.reshape((WIDTH, HEIGHT))
        
Optimal_Policy(Optimal_Value_function())
