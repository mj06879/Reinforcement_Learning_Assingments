A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

C = [[1, 2, 3],
     [4, 5, 6],
     [7, 9, 9]]

B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

lst = [A, B]

for i in range(3):
    for j in range(2, -1 ,-1):
        B[2-j][i] = A[i][j]

if (C in lst):
    print(True)
else:
    print(False)
# for i in B:
#     print(i)
# print(B)