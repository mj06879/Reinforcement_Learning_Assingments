#######################################################################
# Copyright (C)                                                       #
# 2016-2018 Shangtong Zhang(zhangshangtong.cpp@gmail.com)             #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

import numpy as np

WORLD_SIZE = 5
A_POS = [0, 1]
A_PRIME_POS = [4, 1]
B_POS = [0, 3]
B_PRIME_POS = [2, 3]
DISCOUNT = 0.9

# left, up, right, down
ACTIONS = [np.array([0, -1]),
           np.array([-1, 0]),
           np.array([0, 1]),
           np.array([1, 0])]
ACTION_PROB = 0.25

def step(state, action):
    if state == A_POS:
        return A_PRIME_POS, 10
    if state == B_POS:
        return B_PRIME_POS, 5

    next_state = (np.array(state) + action).tolist()
    x, y = next_state
    if x < 0 or x >= WORLD_SIZE or y < 0 or y >= WORLD_SIZE:
        reward = -1.0
        next_state = state
    else:
        reward = 0
    return next_state, reward

def Optimal_Value_function():   
    value = np.zeros((WORLD_SIZE, WORLD_SIZE))
    print(value)
    it = 0
    while True:
        # keep iteration until convergence
        new_value = np.zeros_like(value)
        for i in range(WORLD_SIZE):
            for j in range(WORLD_SIZE):
                values = []
                for action in ACTIONS:
                    (next_i, next_j), reward = step([i, j], action)
                    # bellman equation
                    values.append(ACTION_PROB * (reward + DISCOUNT * value[next_i, next_j]))
                new_value[i, j] = np.max(values)
        if np.sum(np.abs(value - new_value)) < 1e-2:
            break
        value = new_value
        it += 1
        # input("Press Enter to continue...")
        np.set_printoptions(precision=2)
        print(value)
        print()
    print("Converges in {} iterations".format(it))
    return value
        
UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]

def Optimal_Policy(OVF):    # Optimal Value function
    policy = []
    for i in range(WORLD_SIZE):
        for j in range(WORLD_SIZE):
            pol = []
            temp = {}
            for action in ACTIONS:
                (next_i, next_j), reward = step([i, j], action)
                a = ACTION_PROB * (reward + DISCOUNT * OVF[next_i, next_j])
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

if __name__ == '__main__':
    Optimal_Policy(Optimal_Value_function())