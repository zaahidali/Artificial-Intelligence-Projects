############# Zahid Ali #############
############# Kakuros Solver ###########

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model

def Kakuros(list):
    # Creates the model.
    model = cp_model.CpModel()

    # Creating the variables.
    a1 = model.NewIntVar(1, 9, 'a1')
    a2 = model.NewIntVar(1, 9, 'a2')
    a3 = model.NewIntVar(1, 9, 'a3')
    b1 = model.NewIntVar(1, 9, 'b1')
    b2 = model.NewIntVar(1, 9, 'b2')
    b3 = model.NewIntVar(1, 9, 'b3')
    c1 = model.NewIntVar(1, 9, 'c1')
    c2 = model.NewIntVar(1, 9, 'c2')
    c3 = model.NewIntVar(1, 9, 'c3')

	# Constraints	
    model.Add((a1 + b1 + c1) == list[0])
    model.Add((a2 + b2 + c2) == list[1])
    model.Add((a3 + b3 + c3) == list[2])
    model.Add((a1 + a2 + a3) == list[3])
    model.Add((b1 + b2 + b3) == list[4])
    model.Add((c1 + c2 + c3) == list[5])

    # Defined the List For Rows
    First_Row=[a1,a2,a3]
    Sec_Row=[b1,b2,b3]
    Third_Row=[c1,c2,c3]
   
   # Defined the List For Columns
    Column1=[a1,b1,c1]
    Column2=[a2,b2,c2]
    Column3=[a3,b3,c3]
	
	# Creating the Constraints
    model.AddAllDifferent(First_Row)
    model.AddAllDifferent(Sec_Row)
    model.AddAllDifferent(Third_Row)
    model.AddAllDifferent(Column1)
    model.AddAllDifferent(Column2)
    model.AddAllDifferent(Column3)
    
	
	# With Solver and Solves the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
	
	
    if status == cp_model.FEASIBLE:
        return [solver.Value(a1), solver.Value(a2), solver.Value(a3),
                solver.Value(b1), solver.Value(b2), solver.Value(b3),
                solver.Value(c1), solver.Value(c2), solver.Value(c3)]									  
								  			
	# read from input file
with open("kakuro_input.txt", "r") as inputFile:
    elements = []
    for line in inputFile.readlines():
        line = line.strip().split(",")
        for item in line:
            elements.append(int(item))

result = Kakuros(elements)


## Print the results to file	
with open("kakuro_output.txt", "w+")as outputFile:
    outputFile.write("x" + ", " + str(elements[0]) + ", " + str(elements[1]) + ", " + str(elements[2]) + "\n" +
                     str(elements[3]) + ", " + str(result[0]) + ", " + str(result[1]) + ", " + str(result[2]) + "\n" +
                     str(elements[4]) + ", " + str(result[3]) + ", " + str(result[4]) + ", " + str(result[5]) + "\n" +
                     str(elements[5]) + ", " + str(result[6]) + ", " + str(result[7]) + ", " + str(result[8]) )
		
			

	
									  