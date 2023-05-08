#######################################################################
# Copyright (C)                                                       #
# 2016-2018 Shangtong Zhang(zhangshangtong.cpp@gmail.com)             #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

import numpy as np
import random

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
UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]

def Policy_Improvement(OVF):    # Optimal Value function
    policy = []
    for i in range(WORLD_SIZE):   
        for j in range(WORLD_SIZE):
            pol = []       # values for policy
            temp = {}      # dictionary saving the Value function values as keys, and has value list containing actions.
            for action in ACTIONS:
                (next_i, next_j), reward = step([i, j], action)
                # a = ACTION_PROB * (reward + DISCOUNT * OVF[next_i, next_j])
                a = (reward + DISCOUNT * OVF[next_i, next_j])
                pol.append(a)
                if a not in temp:
                    temp[a] = [action]                                  # python list containing np array type.
                else:
                    temp[a].append(action)
            policy.append(temp[np.max(pol)])
    print()
    print("                ********************* Policy: ********************")
    print()

    policy_case = [0 for _ in range(WORLD_SIZE * WORLD_SIZE)]
    for i in range(len(policy)):
        # print(policy[i])
        policy_case[i] = []
        for j in range(len(policy[i])):

            if (policy[i][j] == UP).all():
                policy_case[i].append("up")
            elif (policy[i][j] == DOWN).all():
                policy_case[i].append("down")
            elif (policy[i][j] == LEFT).all():
                policy_case[i].append("left")
            elif (policy[i][j] == RIGHT).all():
                policy_case[i].append("right")

        if (i%5 == 4):        
            print(policy_case[i])
        else:
            print(policy_case[i], end = ',')
    return policy

def Policy_Iteration():      # upgraded figure_3_2()
    V_s = np.zeros((WORLD_SIZE, WORLD_SIZE))              # V(s), Initialization.
    Policy = [[random.choice(ACTIONS)] for _ in range(WORLD_SIZE * WORLD_SIZE)]
    print(V_s)
    it = 0
    policy_stable = False
    while (policy_stable == False):
    
        while True:                                             # Policy Evaluation
            # keep iteration until convergence
            new_value = np.zeros_like(V_s)                    # V(s') ... for compare.
            for i in range(WORLD_SIZE):
                for j in range(WORLD_SIZE):
                    value = 0
                    for action in Policy[WORLD_SIZE*i + j]:
                        (next_i, next_j), reward = step([i, j], action)

                        value += (1/len(Policy[WORLD_SIZE*i + j])) * (reward + DISCOUNT * V_s[next_i, next_j])
                    new_value[i, j] = value

            if np.sum(np.abs(V_s - new_value)) < 1e-2:
                break
            V_s = new_value
        
        it += 1
        
        # input("Press Enter to continue...")
        np.set_printoptions(precision=2)
        print()
        print(V_s)
        new_policy = Policy_Improvement(V_s)                # Improved polciy return 

        if all(np.array_equal(x, y) for x, y in zip(Policy, new_policy)):
            policy_stable = True
        else: 
            Policy = new_policy       

    print("Converges in {} iterations".format(it))
    return value

if __name__ == '__main__':
    Policy_Iteration()