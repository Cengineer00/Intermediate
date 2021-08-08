from helperfunctions import *
from copy import copy, deepcopy

class Sudoku:

    def __init__(self, problem):
        if(type(problem) == str and problem[-3:] == "txt"):
            input_file = open(problem, "r")
            nextline = input_file.readline()

            self.problem = []
            while (nextline != ""):
                self.problem.append([int(num) for num in nextline.split(" ")])

                nextline = input_file.readline()
            self.solution = [row[:] for row in self.problem]

            input_file.close()
        elif(type(problem) == str):
            pass
        else:
            self.problem = problem
            self.solution = problem
    
    def __str__(self):
        for i in range(9):
            for j in range(9):
                if(j == 2 or j == 5):
                    print(self.solution[i][j], end= " | ")
                else:
                    print(self.solution[i][j], end="  ")
            if(i == 2 or i == 5):
                print("")
                print("----------------------------")
            else:
                print("")

        return ""
    
    def solve(self):
        problem_copy = [row[:] for row in self.problem]
        self.solution = sudokusolver(problem_copy)


#EXAMPLE

instance = Sudoku("sudokuinput1.txt")

print(instance)
print("")

instance.solve()

print(instance)