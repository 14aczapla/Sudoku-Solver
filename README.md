# SUDOKU SOLVER
#### Description:
This project is a command-line Sudoku solver that takes an unsolved Sudoku puzzle from a .csv file, solves it with a recursive backtracking algorithm, and presents the completed puzzle in an organized table format. It upholds all traditional Sudoku rules and offers clear console feedback for an engaging user experience.

How It Functions:
File Input – The application requires the location of a .csv file as an argument in the command line. The document should include a 9×9 Sudoku grid with empty squares indicated by 0.
Board Loading – The CSV file is processed and transformed into a two-dimensional array of integers.
Solving Method – The solver looks for the initial vacant cell. It strives to position numbers 1 to 9 in that space, verifying each selection for correctness based on Sudoku regulations (row, column, and 3×3 box limitations).When a number is confirmed as valid, it is positioned, and the solver proceeds recursively.If no number is suitable, the solver backtracks—restoring the cell to 0—and explores an alternative route.
Completion – After solving the puzzle, the finished board is displayed using the tabulate library in a clear, grid-like format.

Functions:
is_empty(board) - Cycles through the board to locate the initial vacant cell (denoted by 0). Gives its position as [row, col]. If all cells are filled, returns None.
is_safe(board, x, y) - Verifies whether the number located at coordinates (x, y) adheres to Sudoku regulations:
No repetitions within a single row.
No repetitions in the same column.
No repetitions within the same 3×3 subgrid.
Returns True if the positioning is valid; otherwise, returns False.
solve(board) - Utilizes the recursive backtracking method:
Locates the subsequent vacant cell.
Tests digits 1–9, checking each using is_safe().
Continues recursively until every cell is accurately filled.
Reverts when a dead end is encountered.
Returns True upon being solved.

main() - If incorrect number of arguments is given or the file type does not match program exits with an appropriate message. Otherwise it prints a solved board.

