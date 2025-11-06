"""
This file will test the functions you have implemented.
"""

import sudoku

def test_parse_input():
    assert sudoku.parse_input('a1') == (0, 0)
    assert sudoku.parse_input('i9') == (8, 8)
    assert sudoku.parse_input('r23') == None
    assert sudoku.parse_input('r') == None
    assert sudoku.parse_input('r2') == None

def test_is_valid():
    t_b = [
        [0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,2],
        [0,0,0,0,0,0,0,0,3],
        [0,0,0,0,0,0,0,0,4],
        [0,0,0,0,0,0,0,0,5],
        [7,8,9,4,5,1,2,3,6],
        [0,0,0,0,0,0,0,0,7],
        [0,0,0,0,0,0,0,0,8],
        [0,0,0,0,0,0,0,0,9]
    ]
    # no conflict on row, col, or square
    assert sudoku.is_valid(t_b, 0, 0, 2) == True
    # conflict on row
    assert sudoku.is_valid(t_b, 0, 0, 1) == False
    # conflict on col
    assert sudoku.is_valid(t_b, 0, 0, 7) == False
    # conflict on square
    assert sudoku.is_valid(t_b, 4, 6, 4) == False
    # conflict in exact space
    assert sudoku.is_valid(t_b, 8, 8, 9) == False

def test_find_empty_cell():
    t_b1 = [
        [0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,2],
        [0,0,0,0,0,0,0,0,3],
        [0,0,0,0,0,0,0,0,4],
        [0,0,0,0,0,0,0,0,5],
        [7,8,9,4,5,1,2,3,6],
        [0,0,0,0,0,0,0,0,7],
        [0,0,0,0,0,0,0,0,8],
        [0,0,0,0,0,0,0,0,9]
    ]
    t_b2 = [
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [7,8,9,4,5,1,2,3,6],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,0]
    ]
    t_b3 = [
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [7,8,9,4,5,1,2,3,6],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1]
    ]
    assert sudoku.find_empty_cell(t_b1) == (0, 0)
    assert sudoku.find_empty_cell(t_b2) == (8, 8)
    assert sudoku.find_empty_cell(t_b3) == None

def test_solve():
    t_b2 = [
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [7,8,9,4,5,1,2,3,6],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,0]
    ]
    t_b3 = [
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [7,8,9,4,5,1,2,3,6],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1],
        [9,8,7,6,5,4,3,2,1]
    ]
    assert sudoku.solve(t_b2) == False
    assert sudoku.solve(t_b3) == True

def test_generate_full_board():
    ref = {
        '1':0, '2':0, '3':0,
        '4':0, '5':0, '6':0,
        '7':0, '8':0, '9':0
    }
    t_b = sudoku.generate_full_board()
    for row in t_b:
        for col in row:
            k = str(col)
            ref[k] += 1
    for key in ref:
        assert ref[key] == 9