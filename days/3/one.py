#!/usr/bin/python3

from typing import List

def main():
    diag = process_input('input.txt')
    gamma = ''
    epsilon = ''

    for idx in range(len(diag[0])):
        vals = list(map(lambda x: x[idx], diag))
        zeros = vals.count('0')
        ones = vals.count('1')
        if zeros > ones:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)

    answer = gamma * epsilon
    print(answer)

        

def process_input(fileName : str) -> List[str]:
    f = open(fileName, 'r')
    nums = []
    for line in f:
        nums.append(line.strip('\n'))
    return nums


if '__main__' in __name__:
    main()
