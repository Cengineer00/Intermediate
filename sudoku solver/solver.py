def numbertoindex(n):
    return [(n//9), n%9]

def indextonumber(i,j):
    return i*9+j

def condition(index, problem):

    number = problem[index[0]][index[1]]

    square_column = (index[1]//3)*3
    square_row = (index[0]//3)*3


    for i in range(3):
        for j in range(3):
            if (problem[square_row+i][square_column+j] == number and index != [square_row+i, square_column+j]):
                return False

    for i in range(9):
        if(problem[i][index[1]] == number and index[0] != i):
            return False

    for j in range(9):
        if(problem[index[0]][j] == number and index[1] != j):
            return False

    return True

def sudokusolver(problem):
    stack = []
    stack.append(0)
    dontvisit = []

    for i in range(9):
        for j in range(9):
            if problem[i][j] != 0:
                dontvisit.append([i, j])

    while (stack != [] and stack[-1]!=81):
        
        index = numbertoindex(stack[-1])
        
        while True:
            if (index in dontvisit):
                stack[-1] += 1
                index = numbertoindex(stack[-1])
                continue
            break
            
        i = problem[index[0]][index[1]]
        
        while (i < 10):
            if (i == 9):
                problem[index[0]][index[1]] = 0
                stack.pop()
                break
            else:
                problem[index[0]][index[1]] = i + 1
                
                if (condition(index, problem)):
                    stack.append(stack[-1] + 1)
                    break
            i += 1
            
    return problem
