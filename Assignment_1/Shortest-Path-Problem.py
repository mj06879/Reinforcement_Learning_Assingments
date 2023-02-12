# Using Bellman Ford Shotest Path discussed in Class.
# All graph nodes are considered as numbers in the code, all work moved over indices scheme. At the end for display Alphabets get added, 
# This was done because input matrix and number of nodes can varry .... so staring wil always be 0 -> S , and Terminal will be (Table_length -1) -> T

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

def Iteration_list_Node_Generator(lst):
    G = {}
    length = len(lst)
    for i in range(length):
        if (i == length-1):
            G['T'] = lst[i]
        else:
            G[alphabet[i]] = lst[i]
    return G
        

def Graph_Node_generator(Indx_Graph):    # Converting All indices into Nodes alphabets 
    G = {}
    length = len(Indx_Graph)
    for key, value in Indx_Graph.items():
        if (key == length-1):
            G['T'] = 'T'
        else:
            if (len(value) <=1):
                if value[0] == length-1:
                    G[alphabet[key]] = 'T'
                else:
                    G[alphabet[key]] = alphabet[value[0]]
            else:
                G[alphabet[key]] = []
                for i in range(len(value)):
                    if value[i] == length-1:
                        G[alphabet[key]].append('T')
                    else: 
                        G[alphabet[key]].append(alphabet[value[i]])
    return G

def Policy_Table_Initializer(Table):     # To initialize the policy Table
    G = {}
    n = len(Table)
    for i in range(n):
        G[i] = None
    return G

Record_Nodes = []           # Record nodes are just to keep noted ... On which nodes  Value function has applied 
def Shortest_path(A):
    G = Graph_generator(A)
    # print(G)
    # print()
    Iteration_list = [math.inf for i in range(len(A)-1)]
    Iteration_list.append(0)
    Nodes = [len(A)-1]                  # current nodes on whose connected nodes Value Function will be applied, starting from Terminal Node
    Record_Nodes.append(len(A)-1)

    itr_num = 1
    new_itr_lst = []
    Policy_table = Policy_Table_Initializer(A)          
    
    # print("Policy at Start: ", Policy_table)
    print("Iteration list at Start: ", Iteration_list)
    print()

    while (new_itr_lst != Iteration_list):
        if itr_num > 1:
            Iteration_list = new_itr_lst.copy()             
        new_itr_lst = Iteration_list.copy()

        for i in Nodes:         # Nodes =[3]   i=3      ... Nodes = [1, 2]   i = 1, 2
            for j in G[i]:      # G[3] = [1, 2]   j = 0, 1    ... G[1] = [0, 3]  , G[2] = [0, 3]
                temp = []
                for k in range(len(A)):      
                    V_x = A[j][k] + Iteration_list[k]           # Value function = d(j, k) + v(k)
                    temp.append(V_x)                            # a list keeping record for min check over all possible Y's --> V(x) = min_{over all possible Y's} {V(y) + m(x, y)}

                lst = []
                m_in = min(temp)                                # getting minimum 
                for index in range(len(temp)):                  # To get the index of minimum and also the if there are two same minimum vlaues. 
                    if (temp[index] == m_in):                   # Here index is the Node
                        lst.append(index)

                if Policy_table[j] == None:                 
                    Policy_table[j] = lst
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
        for idx in Nodes:                       # Updating nodes that will be used in Next Iteration. 
            for j in G[idx]:
                if j not in new and j not in Record_Nodes:   
                    new.append(j)
                    Record_Nodes.append(j)
        Nodes = new
        # print("Nodes: ", Nodes)
        itr_num += 1
    # print ("Policy Table: ", Policy_table)
    # print ("Policy Table: ", Graph_Node_generator(Policy_table))
    # print()
    print ("******************************* Stop Iteration ********************")
    print()
    return [Iteration_list_Node_Generator(Iteration_list), Graph_Node_generator(Policy_table)]


B = [[0, 2, 3, math.inf],
    [2, 0, math.inf, 3],
    [3, math.inf, 0, 2],
    [math.inf, 3, 2, 0]]

A = [[0, 2, 4, 2, math.inf, math.inf, math.inf, math.inf],
    [2, 0, math.inf, math.inf, 7, 4, 6, math.inf],
    [4, math.inf, 0, math.inf, 3, 2, 1,math.inf],
    [2, math.inf, math.inf, 0, 4, 1, 5, math.inf],
    [math.inf, 7, 3, 4, 0, math.inf, math.inf, 7],
    [math.inf, 4, 2, 1, math.inf, 0, math.inf, 9],
    [math.inf, 6, 1, 5, math.inf, math.inf, 0, 6],
    [math.inf, math.inf, math.inf, math.inf, 7, 9, 6, 0]]

def main(input_Table):
    a = Shortest_path(input_Table)
    print("************************* Function Returns ******************************")
    print()
    print("Returns_1: Iteration list")
    print(a[0])
    print()
    print("Returns_2: Policy_Table")
    print(a[1])

main(B)