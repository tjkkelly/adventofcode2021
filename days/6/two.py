#!/usr/bin/python3

from typing import List

def main():
    fishes = process_input('input.txt')
    fishes = aggregate_fishes(fishes)

    for j in range(256):
        new_fish_cnt = fishes[0]
        for i in range(1,len(fishes.keys())):
            fishes[i-1] = fishes[i]
        fishes[6] += new_fish_cnt
        fishes[8] = new_fish_cnt

    t = 0
    for k in fishes.keys():
        t += fishes[k]
    print(t)
        
def aggregate_fishes(fishes):
    m = {i: 0 for i in range(9)}
    for fish in fishes:
        m[fish] += 1
    return m
    
  
def process_input(fileName : str):
    f = open(fileName, 'r')
    return list(map(int, f.readline().strip().split(',')))

if '__main__' in __name__:
    main()
