#!/usr/bin/python3

from typing import List

def main():
    ranges = process_input('input.txt')
    max_x = max(map(lambda x: max(x[0][0], x[1][0]), ranges))
    max_y = max(map(lambda y: max(y[0][1], y[1][1]), ranges))
    board = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]

    for r in ranges:
        start = r[0]
        end = r[1]
        if start[0] == end[0]:
            x_idx = start[0]
            if start[1] < end[1]:
                for i in range(start[1], end[1]+1):
                    board[i][x_idx] += 1
            else:
                for i in range(end[1], start[1]+1):
                    board[i][x_idx] += 1
        elif start[1] == end[1]:
            y_idx = start[1]
            if start[0] < end[0]:
                for i in range(start[0], end[0]+1):
                    board[y_idx][i] += 1
            else:
                for i in range(end[0], start[0]+1):
                    board[y_idx][i] += 1

    cnt = 0
    for row in board:
        for val in row:
            if val > 1:
                cnt +=1

    print(cnt)


    
  

def process_input(fileName : str):
    f = open(fileName, 'r')
    # 959,103 -> 139,923
    ranges = []
    for line in f:
        l, r = map(lambda x: (int(x.split(',')[0]), int(x.split(',')[1])), line.split(' -> '))
        ranges.append((l,r))

    return ranges
    
        


if '__main__' in __name__:
    main()
