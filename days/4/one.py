#!/usr/bin/python3

from typing import List

def main():
    draws, boards = process_input('input.txt')
    
    winning_board = None
    winning_draw = None
    for draw in draws:
        for board in boards:
            for row_idx in range(len(board)):
                for item_idx in range(len(board[row_idx])):
                    if board[row_idx][item_idx] == draw:
                        board[row_idx][item_idx] = None
            if has_board_won(board):
                winning_board = board
                winning_draw = draw
                break
        if winning_board is not None:
            break
    
    s = 0
    for row in winning_board:
        for item in row:
            if item != None:
                s += int(item)
    print(s * int(winning_draw))

def has_board_won(board: List[List[int]]) -> bool:
    for row in board:
        if len(list(filter(lambda x: x != None, row))) == 0:
            return True
    
    for row_idx in range(len(board)):
        column = [board[row_idx] for row in board]
        if len(list(filter(lambda x: x != None, column))) == 0:
            return True

    return False

def process_input(fileName : str):
    f = open(fileName, 'r')
    draws = f.readline().strip().split(',')

    boards = []
    current_board = []
    for line in f:
        if not line.strip():
            boards.append(current_board)            
            current_board = []
        else:
            current_board.append(line.strip().split())

    return draws, boards
        


if '__main__' in __name__:
    main()
