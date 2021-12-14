#!/usr/bin/python3

from typing import List

def main():
    fishes = process_input('input.txt')
    for _ in range(80):
        new_fish_cnt = 0
        for i in range(len(fishes)):
            fishes[i] -= 1
            if fishes[i] < 0:
                fishes[i] = 6
                new_fish_cnt += 1
        #print(new_fish_cnt)
        fishes += [8] * new_fish_cnt

        print(len(fishes))
        
    
  
def process_input(fileName : str):
    f = open(fileName, 'r')
    return list(map(int, f.readline().strip().split(',')))

if '__main__' in __name__:
    main()
