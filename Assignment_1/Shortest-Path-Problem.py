import math
    
alphabet = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'U', 'V', 'W', 'X', 'Y', 'Z', 'T']
def Graph_generator(Table):
    G = {}
    n = len(Table)
    for i in range(n):
        G[i] = []
        for j in range(n):
            if Table[i][j] != 0 and Table[i][j] != math.inf:
                G[i].append(j)
    return G

def Graph_Node_generator(lst):
    G = {}
    for i in range(len(lst)):
        if (i == len(lst)-1):
            G['T'] = lst[i]
        else:
            G[alphabet[i]] = lst[i] 
    return G

def Policy_Table_Initializer(lst):
    G = {}
    for i in range(len(lst)):
        if (i == len(lst)-1):
            G['T'] = 'T'
        else:
            G[alphabet[i]] = None
    return G


def Shortest_path(A):
    G = Graph_generator(A)
    # print(G)
    # print()
    Iteration_list = [math.inf for i in range(len(A)-1)]
    Iteration_list.append(0)
    Nodes = [len(A)-1]
    itr_num = 1
    new_itr_lst = []
    Policy_table = Policy_Table_Initializer(A)
    
    # print("Policy: ", Policy_table)

    print("Start: ", Iteration_list)
    print()

    while (new_itr_lst != Iteration_list):
        if itr_num > 1:
            Iteration_list = new_itr_lst.copy()
        new_itr_lst = Iteration_list.copy()

        for i in Nodes:         # Nodes =[3]   i=3      ... Nodes = [1, 2]   i = 1, 2
            for j in G[i]:      # G[3] = [1, 2]   j = 0, 1    ... G[1] = [0, 3]  , G[2] = [0, 3]
                temp = []
                for k in range(len(A)):      
                    V_x = A[j][k] + Iteration_list[k]

                    # print("V_x:",V_x, "i: ", i, "j: ", j, "k: ",k)
                    temp.append(V_x)
                # print("temp: ",temp)
                # print("ITERATion: ", Iteration_list)

                # lst = []
                # for index in range(len(temp)):
                #     if (temp[index] == min(temp)):
                #         lst.append(index)

                # Policy_table[j] = lst
                new_itr_lst[j] = min(temp)

        '''
        for i in Nodes:         # Nodes =[3]   i=3      ... Nodes = [1, 2]   i = 1, 2
            for j in G[i]:      # G[3] = [1, 2]   j = 0, 1    ... G[1] = [0, 3]  , G[2] = [0, 3]
                temp = []
                for k in range(len(A)):      
                    V_x = A[j][k] + Iteration_list[k]

                    # print("V_x:",V_x, "i: ", i, "j: ", j, "k: ",k)
                    temp.append(V_x)
                print("temp: ",temp)
                # print("ITERATion: ", Iteration_list)
                
                new_itr_lst[j] = min(temp)
        '''

        '''
        for i in range(len(Nodes)):         # Nodes =[7]   i=0
            for j in range(len(G[Nodes[i]])):      # G[i] = [4, 5, 6]   j = 0, 1, 2
                temp = []
                for k in range(len(A)):      
                    V_x = A[G[Nodes[i]][j]][k] + Iteration_list[k]
                    # print("V_x:",V_x, "i: ", i, "j: ", j, "k: ",k)
                    temp.append(V_x)
                # print(temp)
                # print("ITERATion: ", Iteration_list)
                
                new_itr_lst[G[Nodes[i]][j]] = min(temp)
        '''
        
        print("Iteration_list " + str(itr_num), new_itr_lst)
        print()
        new = []
        for idx in Nodes:
            for j in G[idx]:
                if j not in new:
                    new.append(j)
        Nodes = new
        # print("Nodes: ", Nodes)
        itr_num += 1

    return Iteration_list




# A = [[0, 2, 3, math.inf],
#     [2, 0, math.inf, 3],
#     [3, math.inf, 0, 2],
#     [math.inf, 3, 2, 0]]

A = [[0, 2, 4, 2, math.inf, math.inf, math.inf, math.inf],
    [2, 0, math.inf, math.inf, 7, 4, 6, math.inf],
    [4, math.inf, 0, math.inf, 3, 2, 1,math.inf],
    [2, math.inf, math.inf, 0, 4, 1, 5, math.inf],
    [math.inf, 7, 3, 4, 0, math.inf, math.inf, 7],
    [math.inf, 4, 2, 1, math.inf, 0, math.inf, 9],
    [math.inf, 6, 1, 5, math.inf, math.inf, 0, 6],
    [math.inf, math.inf, math.inf, math.inf, 7, 9, 6, 0]]

a = (Shortest_path(A))
# print(Graph_Node_generator(a))
# print(min(math.inf, 1))

# print(min([100, math.inf]))