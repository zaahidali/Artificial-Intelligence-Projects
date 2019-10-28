
#################### Zahid Ali #########################
#################### Futoshiki Solver ##################
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from ortools.sat.python import cp_model

def Futoshiki(Values):
    # Creating the model.
    model = cp_model.CpModel()

    # Creating the variables
    A1 = model.NewIntVar(1, 4, "A1")
    A2 = model.NewIntVar(1, 4, "A2")
    A3 = model.NewIntVar(1, 4, "A3")
    A4 = model.NewIntVar(1, 4, "A4")

    B1 = model.NewIntVar(1, 4, "B1")
    B2 = model.NewIntVar(1, 4, "B2")
    B3 = model.NewIntVar(1, 4, "B3")
    B4 = model.NewIntVar(1, 4, "B4")

    C1 = model.NewIntVar(1, 4, "C1")
    C2 = model.NewIntVar(1, 4, "C2")
    C3 = model.NewIntVar(1, 4, "C3")
    C4 = model.NewIntVar(1, 4, "C4")

    D1 = model.NewIntVar(1, 4, "D1")
    D2 = model.NewIntVar(1, 4, "D2")
    D3 = model.NewIntVar(1, 4, "D3")
    D4 = model.NewIntVar(1, 4, "D4")

    # Creating the Lists For Rows & Columns
    First_Row=[A1,A2,A3,A4]
    Sec_Row=[B1,B2,B3,B4]
    Third_Row=[C1,C2,C3,C4]
    Fourth_Row=[D1,D2,D3,D4]
    First_Column=[A1,B1,C1,D1]
    Sec_Column=[A2,B2,C2,D2]
    Third_Column=[A3,B3,C3,D3]
    Fourth_Column=[A4,B4,C4,D4]


    # Creating the Constraints
    model.AddAllDifferent(First_Row)
    model.AddAllDifferent(Sec_Row)
    model.AddAllDifferent(Third_Row)
    model.AddAllDifferent(Fourth_Row)

    model.AddAllDifferent(First_Column)
    model.AddAllDifferent(Sec_Column)
    model.AddAllDifferent(Third_Column)
    model.AddAllDifferent(Fourth_Column)

    dic = {"A1": A1,"A2": A2,"A3": A3,"A4": A4,"B1": B1,"B2": B2,"B3": B3,"B4": B4,"C1": C1,"C2": C2,"C3": C3,"C4": C4, "D1": D1,"D2": D2,"D3": D3,"D4": D4}

    for value1, value2 in Values:
        if value2.isdigit():
            model.Add(dic[value1] == int(value2))
        else:
            model.Add(dic[value1] > dic[value2])

    # With a solver solves the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        return [solver.Value(A1), solver.Value(A2), solver.Value(A3), solver.Value(A4)
                , solver.Value(B1), solver.Value(B2), solver.Value(B3), solver.Value(B4)
                , solver.Value(C1), solver.Value(C2), solver.Value(C3), solver.Value(C4)
                , solver.Value(D1), solver.Value(D2), solver.Value(D3), solver.Value(D4)]

				

with open("futoshiki_input.txt", "r") as inputFile:
    Numbers = []
    for line in inputFile.readlines():
        line = line.replace("\n", "")
        line = line.split(", ")
        Numb = (line[0],line[1])
        Numbers.append(Numb)


output = Futoshiki(Numbers)
		
#print the output to the file
with open("futoshiki_output.txt", "w+")as outputFile:
    outputFile.write(str(output[0]) + ", " + str(output[1]) + ", " + str(output[2]) + ", " + str(output[3]) + "\n" +
                     str(output[4]) + ", " + str(output[5]) + ", " + str(output[6]) + ", " + str(output[7]) + "\n" +
                     str(output[8]) + ", " + str(output[9]) + ", " + str(output[10]) + ", " + str(output[11]) + "\n" +
                     str(output[12]) + ", " + str(output[13]) + ", " + str(output[14]) + ", " + str(output[15]))		
