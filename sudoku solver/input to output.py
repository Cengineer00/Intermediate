import solver as solver
import time

start_time = time.time()

f = open("sudokuoutput.txt", "a")

for i in range(4):
    input_file = open("sudokuinput"+str(i+1)+".txt", "r")
    nextline = input_file.readline()

    problem = []
    while (nextline != ""):
        problem.append([int(num) for num in nextline.split(" ")])

        nextline = input_file.readline()

    input_file.close()

    solution = solver.sudokusolver(problem)
    for i in range(9):
        for j in range(9):
            f.write(str(solution[i][j]) + " ")
        f.write("\n")

    f.write("\n---------------------------\n")

f.close()

print("--- %s seconds ---" % (time.time() - start_time))
