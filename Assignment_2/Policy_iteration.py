import numpy as np

# np.amax() gives the maximum in array. index of maximum return by np.argmax()

# To get if max at more places: np.where(VnextState === np.amax(VnextState))[0].tolist()
#   it returns the in tuple datatype.(array[1, 2, ..], dtype = int64)    
#   ... The [0] we used because we're only concerned with first value that is the array. 

# WORLD_SIZE = 5
# a = np.max([2, 3, 3, 3,  1])
# value = np.zeros((WORLD_SIZE, WORLD_SIZE))
# value[3][0] = 'left'
# print(value)

print(19%5)

# ACTIONS = [np.array([0, -1]),
#            np.array([-1, 0]),
#            np.array([0, 1]),
#            np.array([1, 0])]

# for action in ACTIONS:
#     # print(action.tolist())
#     # print(type(action))
#     if action.tolist() == [0, -1]:
#         print("up")
# print(type(ACTIONS[0])) 