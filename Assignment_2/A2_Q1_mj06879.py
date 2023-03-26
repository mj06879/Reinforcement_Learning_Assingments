import GridWorld_3_5 as Opt_V_F
import numpy as np
UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]

def Optimal_Policy(OVF):    # Optimal Value function
    policy = []
    for i in range(Opt_V_F.WORLD_SIZE):
        for j in range(Opt_V_F.WORLD_SIZE):
            pol = []
            temp = {}
            for action in Opt_V_F.ACTIONS:
                (next_i, next_j), reward = Opt_V_F.step([i, j], action)
                a = reward + Opt_V_F.DISCOUNT * OVF[next_i, next_j]
                # a = OVF[next_i, next_j]
                pol.append(a)
                if a not in temp:
                    temp[a] = [action.tolist()]
                else:
                    temp[a].append(action.tolist())
            policy.append(temp[np.max(pol)])
    print()
    print("                ********************* Optimal Policy: ********************")
    print()

    for i in range(len(policy)):
        # print(policy[i])
        for j in range(len(policy[i])):
            if policy[i][j] == UP:
                policy[i][j] = "up"
            elif policy[i][j] == DOWN:
                policy[i][j] = "down"
            elif policy[i][j] == LEFT:
                policy[i][j] = "left"
            elif policy[i][j] == RIGHT:
                policy[i][j] = "right"

        if (i%5 == 4):        
            print(policy[i])
        else:
            print(policy[i], end = ',')

Optimal_Policy(Opt_V_F.figure_3_5())