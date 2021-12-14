#!/usr/bin/python3

from typing import List

def main():
    positions = process_input('input.txt')
    cap = max(positions)
    best_mpg = None
    for pos in range(cap):
        cost = sum(list(map(lambda x: sum(range(1,abs(x-pos)+1)), positions)))
        if not best_mpg:
            best_mpg = cost
        else:
            best_mpg = min(best_mpg, cost)
    print(best_mpg)

def process_input(fileName : str):
    f = open(fileName, 'r')
    return list(map(int, f.readline().strip().split(',')))

if '__main__' in __name__:
    main()
