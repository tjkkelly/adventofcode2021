#!/usr/bin/python3

from typing import List

def main():
    diag = process_input('input.txt')
    oxygen = diag[:]
    co2 = diag[:]

    for idx in range(len(oxygen[0])):
        vals = list(map(lambda x: x[idx], oxygen))
        zeros = vals.count('0')    
        ones = vals.count('1')
        if zeros > ones:
            oxygen = list(filter(lambda x: x[idx] == '0', oxygen))
        else:
            oxygen = list(filter(lambda x: x[idx] == '1', oxygen))
        
        if len(oxygen) == 1:
            break

    for idx in range(len(co2[0])):
        vals = list(map(lambda x: x[idx], co2))
        zeros = vals.count('0')    
        ones = vals.count('1')
        if zeros > ones:
            co2 = list(filter(lambda x: x[idx] == '1', co2))
        else:
            co2 = list(filter(lambda x: x[idx] == '0', co2))
        
        if len(co2) == 1:
            break

    oxygen = int(oxygen[0], base=2)
    co2 = int(co2[0], base=2)

    answer = oxygen * co2
    print(answer)

        

def process_input(fileName : str) -> List[str]:
    f = open(fileName, 'r')
    nums = []
    for line in f:
        nums.append(line.strip('\n'))
    return nums


if '__main__' in __name__:
    main()
