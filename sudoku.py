"""
This file will contain the main function
"""
import sys
import random
import datetime
from pyfiglet import Figlet
from colorama import Back, Style
from typing import List, Optional
from copy import deepcopy


def which_game_function()-> str:
    """
    This function is called to help the player decide which path to choose for the game.
    parameter: None
    returns either '1' or '2' for the choice in the game
    """
    f_str_1 = "\nWould you like to play SUDOKU or enter a SUDOKU puzzle to be solved for you?\n"
    f_str_2 = "For a puzzle to PLAY, ENTER 1 \n"
    f_str_3 = "To enter a puzzle to SOLVE by the computer, ENTER 2 \n"
    f_str_4 = "To quit the program ENTER q\n"
    f_str = f_str_1 + f_str_2 + f_str_3 + f_str_4
    while True:
        request = input(f_str)
        if request.lower() == 'q':
            print("Goodbye.")
            sys.exit(0)
        if request != '1' and request != '2':
            print("You must type 1 or 2")
        else:
            return request

def level_to_play():
    # difficulty level query
    while True:
        levels = ['1', '2', '3']
        level = input("DIFFICULTY:\n1. EASY\n2. MEDIUM\n3. HARD\nEnter a value for difficulty. ")
        if level not in levels:
            print("Invalid answer, try again.")
            continue
        # the random number generated represents how many squares will be filled in the puzzle
        if level == '1':
            return random.randrange(36, 46)
        if level == '2':
            return random.randrange(27, 36)
        if level == '3':
            return random.randrange(20, 27)

def enter_puzzle_to_solve() -> int:
    def process_string_to_list(s) -> List:
        # gate to ensure s is of length 9
        if len(s) != 9:
            return [0 for _ in range(9)]

        # gate to ensure string is all numeric
        if s.isnumeric():
            int_list = [int(c) for c in s]

            # account for repeats
            length = len(set(int_list))
            if length == 9:
                return int_list
            # error handling for repeats and deal with zeroes
            zeroes = 0
            for i in int_list:
                if i == 0:
                    zeroes += 1
            if length + zeroes == 10:
                return int_list

        return [0 for _ in range(9)]

    print("To enter a puzzle there will be nine prompts for each row from top to bottom, going left to right.")
    print("Enter each row as a continuous string, like a string of 123456789")
    print("If you have a cell to be solved enter a zero in that space,\nso the string above with 3, 6, and 9 missing would be 120450780")
    board = []
    while True:
        board = []
        for i in range(1, 10):
            row = process_string_to_list(input(f"Enter row {i} left to right as continuous numbers with no commas: "))
            board.append(row)
        print_labeled_board(board)
        valid = input("Is your board correct? y/n: ")
        if valid.lower() == 'y':
            break
        else:
            print("Try to enter again.")
            continue
    return board

def print_sudoku_instructions():
    # format fancy title:
    fig = Figlet()
    fonts = fig.getFonts()
    fig.setFont(font=random.choices(fonts, k=1)[0])
    print(Back.BLUE + fig.renderText("SUDOKU") + Style.RESET_ALL)

    # instructions:
    print("This is the Sudoku program.\nTo play you must fill in the blank spaces of a 9x9 grid")
    print("with numbers from 1 - 9, such that each rule below is satisfied:\n")
    print("======================================================")
    print(Back.BLUE + "|                      Rules                         |" + Style.RESET_ALL)
    print("======================================================\n")
    print("1. Each row must only have one occurrence of the numbers 1 thru 9")
    print("2. Each column must only have one occurrence of the numbers 1 thru 9")
    print("3. Each 3x3 grid separated by double lines must only have one occurrence of the numbers 1 thru 9")
    print("The grid is labeled with columns a thru i and the rows labeled 1 thru 9\n")
    print("This program can be used in two ways:")
    print("1. A board is created by the program for the player to solve based on a chosen level of difficulty.")
    print("2. A player may choose to enter a board to play and if stuck the program can determine the solution or verify no unique solution exists.")

    selection = which_game_function()
    if selection == '1':
        # want_to_play()
        return level_to_play()
    if selection == '2':
        return enter_puzzle_to_solve()

# printing the filled in board
def print_labeled_board(board):
    """
    This function takes in the current board and prints the labeled board to the CLI.
    """
    print("    a   b   c    d   e   f    g   h   i")
    print("  +-------------------------------------+")
    # process the board and print each row
    for i, row in enumerate(board):
        row_str = f"{i+1} | "
        for j, val in enumerate(row):
            if j == 2 or j == 5:
                row_str += f"{val if val != 0 else ' '} || "
            else:
                row_str += f"{val if val != 0 else ' '} | "
        print(row_str)
        print("  +-------------------------------------+")
        if i == 2 or i == 5:
            print("  +-------------------------------------+")

# handle the input coordinates
def parse_input(move: str):
    """
    This function takes in a coordinate ex:"f9" to place a number into the board at the destination coordinate.
    """
    if len(move) != 2:
        return None
    col_c, row_c = move[0].lower(), move[1]
    if col_c < 'a' or col_c > 'i':
        return None
    if row_c < '1' or row_c > '9':
        return None
    col = ord(col_c) - ord('a')
    row = int(row_c) - 1
    return row, col

# check the validity of the number in the position on the board.
def is_valid(board: List[List[int]], row: int, col: int, num: int) -> bool:
    # check the row and column:
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    # else
    return True

# takes in the board and returns a tuple of row, col location for empty cell or NONE for filled out board.
def find_empty_cell(board: List[List[int]]) -> Optional[tuple[int, int]]:
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def solve(board: List[List[int]]) -> bool:
    """
    This function returns a bool for whether the board is solvable.
    And if it is solvable, the board will be solved in place.
    ** NOTE: make a copy of the board to be solved, if needing the original board.
    """
    # looks for empty cells
    empty = find_empty_cell(board)
    if not empty:
        return True
    else:
        row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0

    return False


# generates a full board, this is the filled in solution.
def generate_full_board() -> List[List[int]]:
    board = [[0 for _ in range(9)] for _ in range(9)]

    def fill(board: List[List[int]]) -> bool:
        empty = find_empty_cell(board)
        if not empty:
            return True
        row, col = empty
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for n in numbers:
            if is_valid(board, row, col, n):
                board[row][col] = n
                if fill(board):
                    return True
                board[row][col] = 0
        return False

    fill(board)
    return board

def count_solutions(board: List[List[int]], limit: int = 2) -> int:
    """
    Used during puzzle generation to ensure uniqueness
    Internally used by the puzzle generator, not exposed to user
    This function returns a number of viable solutions.
    """
    def helper(board: List[List[int]], count: list[int]) -> bool:
        # Early exit if we don't care about solutions beyond limit
        if count[0] >= limit:
            return True

        empty = find_empty_cell(board)
        if not empty:
            count[0] += 1
            return False

        row, col = empty
        # iterate over each number 1-9, if it is valid, place it.
        # recall helper on the board
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                if helper(board, count):
                    board[row][col] = 0
                    return True
                board[row][col] = 0

        return False

    count = [0]
    helper(board, count)
    return count[0]


def generate_puzzle(min_clues: int = 25):
    """
    uses generate_full_board, removes one cell at a time
    calls count_solutions to ensure only one solution remains.
    """
    board = generate_full_board()
    positions = [(r,c) for r in range(9) for c in range(9)]
    random.shuffle(positions)

    # iterate through
    for row, col in positions:
        non_empty_cells = sum(1 for row_ in board for cell in row_ if cell != 0)
        if non_empty_cells <= min_clues:
            break

        # temporarily remove info from the cell (set to 0)
        temp_removed_value = board[row][col]
        board[row][col] = 0

        # make copy of board to test uniqueness
        b_copy = deepcopy(board)

        # count solutions if not unique, put it back
        if count_solutions(b_copy) != 1:
            board[row][col] = temp_removed_value

    return board


def play_sudoku(puzzle: List[List[int]], solution: List[List[int]]) -> None:
    """
    This function takes in the puzzle board and the solution board and compares to ensure solution between moves.
    """
    current = deepcopy(puzzle)
    print_labeled_board(current)

    while True:
        print("\nHINT: if you mess up adding a number, try that square again and make the value zero to erase the mistake.\n")
        move = input("\nEnter move (ex: b2 8), or enter 'q' to quit: ").strip().lower()
        if move == 'q':
            sure = input("\n are you sure you want to quit, y / n ").strip().lower()
            if sure == 'y':
                print("Thanks for playing, here is the solution to the board!")
                print_labeled_board(solution)
                print("Below is the amount of time spent on the puzzle")
                break

        parts = move.split()
        if len(parts) != 2:
            print("Invalid input. Format should be like a5 4")
            continue

        coord, val_str = parts
        pos = parse_input(coord)
        if not pos or not val_str.isdigit():
            print("Invalid coordinate or value. Try again.")
            continue

        row, col = pos
        value = int(val_str)

        if puzzle[row][col] != 0:
            print("You can't change a pre-filled square.")
            continue

        if puzzle[row][col] == 0 and value == 0:
            current[row][col] = value
            print_labeled_board(current)
            continue

        if not (1 <= value <= 9):
            print("Enter a number between 1 and 9.")
            continue

        current[row][col] = value
        print_labeled_board(current)

        if current == solution:
            print("\nPuzzle completed correctly! Great job!")
            break


def main():
    """
    Main running of the game:
    """
    while True:
        user_input = print_sudoku_instructions()
        if type(user_input) == int:
            puzzle = generate_puzzle(min_clues = user_input)
            solution = deepcopy(puzzle)
        else:
            puzzle = user_input
            solution = deepcopy(user_input)

        if solve(solution):
            start = datetime.datetime.now()
            play_sudoku(puzzle, solution)
            end = datetime.datetime.now()
            duration = end - start
            h = duration.seconds // 3600
            m = (duration.seconds - (h*3600)) // 60
            s = (duration.seconds - (h*3600) - (m*60))
            print(f"Time to completion (hh:mm:ss): {h:02d}:{m:02d}:{s:02d}")
        else:
            print("There is no solution for that board.")
        again = input("Enter y to play again or any other key to QUIT ")
        if again.lower() == 'y' or again.lower() == 'yes':
            continue
        else:
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()