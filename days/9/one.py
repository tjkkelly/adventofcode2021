#!/usr/bin/python3

from typing import List

def main():
    height_map = process_input('input.txt')
    low_points = []
    total_risk = 0
    
    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            is_low = is_low_point(height_map, i, j)
            if is_low:
                val = height_map[i][j]
                total_risk += val + 1

    print(total_risk)

def is_low_point(height_map, i, j):
    is_low = True
    val = height_map[i][j]
    valid_dirs = get_valid_dirs(height_map, i, j)

    for d in valid_dirs:
        if d == 'l' and val >= height_map[i][j-1]:
            is_low = False
            break
        if d == 'r' and val >= height_map[i][j+1]:
            is_low = False
            break
        if d == 'u' and val >= height_map[i-1][j]:
            is_low = False
            break
        if d == 'd' and val >= height_map[i+1][j]:
            is_low = False
            break
    return is_low

def get_valid_dirs(height_map, i, j):
    valid_dirs = []
    if i != 0:
        valid_dirs += 'u'
    if j != 0:
        valid_dirs += 'l'
    if i != len(height_map) - 1:
        valid_dirs += 'd'
    if j != len(height_map[i]) - 1:
        valid_dirs += 'r'
    return valid_dirs
  
def process_input(fileName : str):
    f = open(fileName, 'r')
    output = []
    # 5456789349886456890123985435578996543213456789656899996467789234989765442345789778999989652349879899
    for line in f:
        output.append(list(map(int,list(line.strip()))))
    
    return output


if '__main__' in __name__:
    main()
