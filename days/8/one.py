#!/usr/bin/python3

from typing import List

def main():
    gibberish = process_input('input.txt')

    res = 0
    for gib in gibberish:
        unique = gib[0]
        output = gib[1]
        mapping = get_mapping(unique)
        val = "0"
        for small_gib in output:
            lookup = {small_gib: v for k, v in mapping.items() if set(k) == set(small_gib)}
            val += str(lookup[small_gib])
        print(f"adding {int(val)}")
        res += int(val)

    print(res)

def get_mapping(unique):
    len_map = {6:[0,6,9], 2:[1], 5:[2,3,5], 4:[4], 3:[7], 7:[8]}

    mapping = {}
    inverse_mapping = {}
    for u in unique:
        if len(len_map[len(u)]) == 1:
            mapping[u] = len_map[len(u)][0]
            inverse_mapping[len_map[len(u)][0]] = u

    len_5 = list(filter(lambda x: len(x) == 5, unique))
    len_6 = list(filter(lambda x: len(x) == 6, unique))
    for item in len_5:
        if set(inverse_mapping[1]).union(set(item)) == set(item):
            mapping[item] = 3
            inverse_mapping[3] = item

    # 1, 3, 4, 7, 8 are done
    for item in len_6:
        if set(inverse_mapping[3]).union(set(inverse_mapping[4])) == set(item):
            mapping[item] = 9
            inverse_mapping[9] = item

    # 1, 3, 4, 7, 8, 9 are done
    for item in len_6:
        if item in mapping.keys():
            continue
        if set(inverse_mapping[7]).union(set(item)) == set(item):
            mapping[item] = 0
            inverse_mapping[0] = item

    # 0, 1, 3, 4, 7, 8, 9 are done
    for item in len_6:
        if item in mapping.keys():
            continue
        else:
            mapping[item] = 6
            inverse_mapping[6] = item
    
    # 0, 1, 3, 4, 6, 7, 8, 9 are done
    for item in len_5:
        if item in mapping.keys():
            continue
        elif len(set(inverse_mapping[6]).union(set(item))) == len(set(inverse_mapping[8])):
            mapping[item] = 2
            inverse_mapping[2] = item
    
    for item in unique:
        if item not in mapping.keys():
            mapping[item] = 5
            
    return mapping
  
def process_input(fileName : str):
    f = open(fileName, 'r')
    # beacf afbd bcead cgefa ecdbga efb gbfdeac ecgfbd acbdfe fb | bf efb bgecdfa egcfa
    ret = []
    for line in f:
        signals, outputs = line.strip().split(' | ')
        signals = signals.split(' ')
        outputs = outputs.split(' ')
        ret.append([signals, outputs])
    return ret
        

if '__main__' in __name__:
    main()
