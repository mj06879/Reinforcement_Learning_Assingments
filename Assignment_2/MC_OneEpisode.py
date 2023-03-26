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
grid = np.zeros(HEIGHT * WIDTH)
gridCounts = np.zeros(HEIGHT * WIDTH)
avgCounts = np.zeros(HEIGHT * WIDTH)

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
#         print(1, next_state, reward)
        if next_state == -1:
            return episode, episodeReward
        else:
            episode.append(next_state)
            episodeReward.append(reward)
        state = next_state
    return episode, episodeReward



state = startingState()
e, eR = runEpisode(state)
print(e, eR, sep = "\n\n")

