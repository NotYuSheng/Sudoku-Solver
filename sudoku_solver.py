# 26/05/2021
# Sudoku Solver
# Simple back tracking method
# https://www.youtube.com/watch?v=G_UYXzGuqvM&ab_channel=ComputerphileComputerphileVerified
# Interesting problem encountered, unable to create have the function (bruteforce) return table
# due to return None from recursive back track
def possible(table: list, row: int, column: int, number: int) -> bool:
    """Returns if possible to insert number into position as per rules"""

    # Rule1: Row
    for index in range(9):
        if table[column][index] == number:
            return False

    # Rule2: Column
    for index in range(9):
        if table[index][row] == number:
            return False

    # Rule3: Square
    row_square = (row // 3) * 3
    column_square = (column // 3) * 3
    for row_index in range(0, 3):
        for column_index in range(0, 3):
            if table[column_index + column_square][row_index + row_square] == number:
                return False

    return True


def bruteforce(table: list):
    """Bruteforce and print solution, read script header"""

    for column in range(9):
        for row in range(9):
            if table[column][row] == 0:
                for number in range(1, 10):
                    if possible(table, row, column, number):
                        table[column][row] = number
                        bruteforce(table)
                        table[column][row] = 0
                # All possibilities attempted, yet not possible
                return
    print(table)


def main():
    table = [[6, 7, 2, 0, 0, 1, 9, 8, 4],
             [0, 3, 1, 0, 0, 0, 0, 0, 0],
             [0, 4, 0, 0, 2, 0, 0, 0, 3],
             [4, 0, 5, 0, 0, 0, 3, 0, 8],
             [9, 2, 0, 3, 7, 0, 5, 0, 0],
             [7, 6, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 4, 9, 0, 8, 3, 2],
             [3, 0, 6, 0, 0, 0, 0, 4, 5],
             [0, 0, 4, 0, 5, 0, 1, 9, 6]]
    bruteforce(table)


if __name__ == "__main__":
    main()
