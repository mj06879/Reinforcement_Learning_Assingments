# we are assuming that the starting element is "x", we can state validity at any stage either one participants has taken its turn or both of has. 
# Starting state, means when all positions are empty will be considered as valid state.

def Dict_to_list(input_dict):
    lst = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    for key, value in input_dict.items():
        if key == 'A1':
            lst[0][0] = value
        elif key == 'A2':
            lst[0][1] = value
        elif key == 'A3':
            lst[0][2] = value
        elif key == 'B1':
            lst[1][0] = value
        elif key == 'B2':
            lst[1][1] = value
        elif key == 'B3':
            lst[1][2] = value
        elif key == 'C1':
            lst[2][0] = value
        elif key == 'C2':
            lst[2][1] = value
        elif key == 'C3':
            lst[2][2] = value
    return lst

def List_to_dict(input_lst):
    dct = {
        'A1': input_lst[0][0], 'A2': input_lst[0][1], 'A3': input_lst[0][2],
        'B1': input_lst[1][0], 'B2': input_lst[1][1], 'B3': input_lst[1][2],
        'C1': input_lst[2][0], 'C2': input_lst[2][1], 'C3': input_lst[2][2]}

    return dct

def Valid_state_check(dict_input):

    A = Dict_to_list(dict_input)
    sum_in_rows_x = [0, 0, 0]
    sum_in_colms_x =  [0, 0, 0]
    sum_in_diagonals_x = [0, 0]
    sum_in_rows_o = [0, 0, 0]
    sum_in_colms_o = [0, 0, 0]
    sum_in_diagonals_o = [0, 0]
    total_o = 0
    total_x = 0

    for i in range(3):
        for j in range(3):
            if A[i][j] == 'x':
                total_x += 1
                sum_in_rows_x[i] += 1
                sum_in_colms_x[j] += 1
                if i == j:
                    sum_in_diagonals_x[0] += 1
                if (i== 0 and j == 2) or (i == 2 and j == 0) or (i == j == 1):
                    sum_in_diagonals_x[1] += 1

            elif A[i][j] == 'o':
                total_o += 1
                sum_in_rows_o[i] += 1
                sum_in_colms_o[j] += 1
                if i == j:
                    sum_in_diagonals_o[0] += 1
                if (i== 0 and j == 2) or (i == 2 and j == 0) or (i == j == 1):
                    sum_in_diagonals_o[1] += 1
    
    x_win = 0
    o_win = 0
    if (
        (sum_in_rows_x.count(3) == 1 and sum_in_colms_x.count(3) == sum_in_diagonals_x.count(3) == 0) 
        or (sum_in_colms_x.count(3) == 1 and sum_in_rows_x.count(3) == sum_in_diagonals_x.count(3) == 0)
        or (sum_in_diagonals_x.count(3) == 1 and sum_in_rows_x.count(3) == sum_in_colms_x.count(3) == 0)
    ):  
        x_win = 1
    if (
        (sum_in_rows_o.count(3) == 1 and sum_in_colms_o.count(3) == sum_in_diagonals_o.count(3) == 0) 
        or (sum_in_colms_o.count(3) == 1 and sum_in_rows_o.count(3) == sum_in_diagonals_o.count(3) == 0)
        or (sum_in_diagonals_o.count(3) == 1 and sum_in_rows_o.count(3) == sum_in_colms_o.count(3) == 0)
    ):  
        o_win = 1

    # print("sum_in_rows_x: ",sum_in_rows_x)  
    # print("sum_in_rows_o", sum_in_rows_o)  
    # print("X_win = ", x_win)
    # print("o_win = ", o_win)

    valid = 0
    if (total_x  == 0 and total_o == 0):  #starting state
        valid = 1

    elif (
        (((total_x - total_o) == 1 ) or ((total_x - total_o) == 0 )) and (not(x_win == o_win == 1))   # |x| - |o| \in  [0,1]  and checking as both cannot win. 
    ):
        valid = 1

    # print(valid)
    return [A, valid]

def Rotationally_equivalent_generator(args):
    # args[0]   ---> Table
    # args[1]   ---> valid

    Current_Table = (args[0]).copy()
    Rotational_equivalents = [args[0]]

    if args[1] == 0:
        print("The given state is not a valid state of Tic-Tac-Toe table.")                   
        return ([{}])
    elif args[1] == 1:
        count = 1
        while(count < 4):
            temp = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            for i in range(3):
                for j in range(2, -1, -1):
                    temp[2-j][i] = Current_Table[i][j]

            if temp in Rotational_equivalents:
                break
            else:
                Rotational_equivalents.append(temp)
                Current_Table = temp
            count += 1

    Rotational_equivalents.pop(0)
    for i in range(len(Rotational_equivalents)):
        print("**************** Rotationally Equivalent Matrix: " + str(i +1 ) + " *******************")
        print()
        for j in Rotational_equivalents[i]:
            print(j)
        print()

    return [List_to_dict(i) for i in Rotational_equivalents]

def main(Table_entries):
    print("*************************** Original Table ***************************")
    print()
    valid_state_result = Valid_state_check(Table_entries)
    for i in valid_state_result[0]:
        print(i)
    print()
    print("Returns: ", Rotationally_equivalent_generator(valid_state_result))


# input = {'A2': 'x', 'B3': 'o', 'B2': 'x', 'A1': 'x', 'A3': 'o', 'B1': 'o'}
input = {'A2': 'x', 'B1': 'o', 'B3': 'o', 'C2': 'x'}
# input = {'A1': 'x', 'A2': 'o', 'B2': 'o'}
# input = {'A1': 'o', 'A2': 'x', 'A3': 'o', 'C1': 'x', 'C2': 'o', 'C3': 'x'}
# input = {'B2': 'o'}
main(input)
