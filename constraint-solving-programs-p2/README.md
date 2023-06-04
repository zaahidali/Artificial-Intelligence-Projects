# Kakuros and Futoshiki Solver

This folder contains two project codes, the Kakuros Solver and the Futoshiki Solver. Both solvers are implemented using the ortools library, specifically the cp_model module, to solve constraint satisfaction problems.

# 1. Futoshiki Solver

The Futoshiki Solver is a program that solves Futoshiki puzzles. Futoshiki is a logic-based number puzzle similar to Sudoku, but with additional inequality constraints. The goal of the puzzle is to fill the grid with numbers while satisfying the given constraints.

## Usage

To use the Futoshiki Solver, follow the steps below:

1. Prepare the input file `futoshiki_input.txt` with the Futoshiki puzzle and constraints. The file should have the following format:

```
B2, 1
D4, 2
A1, A2
A4, B4
C2, C1
D2, C2
```

- Each line represents a constraint.
- The format of a constraint is `cell1, cell2`, where `cell1` and `cell2` represent the cells involved in the constraint.
- If a cell has a number, it is represented as `cell, number`.

2. Run the program by executing `python futoshiki_solver.py` in the command line.

3. The program will solve the Futoshiki puzzle and generate the output file `futoshiki_output.txt` with the solution. The output file will contain the filled grid with the numbers that satisfy all the constraints.

## Example

Suppose we have the following Futoshiki puzzle with the given constraints:

```
   |   |   |
---+---+---+---
   |   | 2 |
---+---+---+---
   | 3 |
```

To represent this puzzle in `futoshiki_input.txt`, we would have the following content:

```
B2, 2
C1, B2
C2, A2
```

Running the Futoshiki Solver program would generate the following solution in `futoshiki_output.txt`:

```
   |   |   |
---+---+---+---
   |   | 2 |
---+---+---+---
  2| 3 |
```

## Constraints

The Futoshiki Solver handles the following types of constraints:

1. Cell with a Number: Represents a cell with a fixed number. Example: `B2, 2`

2. Less Than Constraint: Represents a constraint where one cell must be less than another. Example: `C1, B2`

3. Greater Than Constraint: Represents a constraint where one cell must be greater than another. Example: `C2, A2`

The solver uses the **orthogonal tools (ortools)** library, specifically the **cp_model** module, to model and solve the Futoshiki puzzle as a constraint satisfaction problem.

# 2. Kakuros Solver

The Kakuros Solver is a program that solves Kakuro puzzles. Kakuro is a logic-based number puzzle that resembles a crossword puzzle, where the goal is to fill the grid with numbers that satisfy the given sum constraints for each row and column.

## Usage

To use the Kakuros Solver, follow the steps below:

1. Prepare the input file `kakuro_input.txt` with the Kakuro puzzle constraints. The file should have the following format:

```
22, 18, 7
20, 19, 8
```

- Each line represents a row or column with the sum constraint.
- The format of a constraint is a comma-separated list of numbers, where each number represents the sum of the cells in the corresponding row or column.

2. Run the program by executing `python kakuros_solver.py` in the command line.

3. The program will solve the Kakuro puzzle and generate the output file `kakuro_output.txt` with the solution. The output file will contain the filled grid that satisfies all the sum constraints.

## Example

Suppose we have the following Kakuro puzzle with the given sum constraints:

```
   |   |   |
---+---+---+---
   |   |   |
---+---+---+---
   |   |
```

To represent this puzzle in `kakuro_input.txt`, we would have the following content:

```
15, 16, 6
10, 5, 12
```

Running the Kakuros Solver program would generate the following solution in `kakuro_output.txt`:

```
   |   |   |
---+---+---+---
   |   |   |
---+---+---+---
   |   |
```

## Constraints

The Kakuros Solver handles the following types of constraints:

1. Row Sum Constraint: Represents the sum of the numbers in a row. Example: `15, 16, 6`

2. Column Sum Constraint: Represents the sum of the numbers in a column. Example: `10, 5, 12`

The solver uses the **orthogonal tools (ortools)** library, specifically the **cp_model** module, to model and solve the Kakuro puzzle as a constraint satisfaction problem.

Please note that the Kakuros Solver assumes that the input puzzle has a unique solution. If the puzzle is not solvable or has multiple solutions, the program may not provide accurate results.

Feel free to explore different Kakuro puzzles by modifying the input file and running the solver program. Enjoy solving Kakuros!