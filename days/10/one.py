#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

from typing import List

def main():
    score_mapping = {']': 57, '}': 1197, ')': 3, '>': 25137}

    chunks = process_input('input.txt')
    score = 0
    for chunk in chunks:
        is_val, err = is_valid(chunk)
        if not is_val:
            score += score_mapping[err]
    print(score)



def is_valid(chunk):
    mapping = {']':'[', '}':'{', ')':'(', '>':'<'}
    stack = []
    for val in chunk:
        if val in mapping.values():
            stack.append(val)
        else:
            if len(stack) == 0 or mapping[val] != stack[-1]:
                return False, val
            else:
                stack.pop()
    
    # if len(stack) != 0:
    #     return False

    return True, None

  
def process_input(fileName : str):
    f = open(fileName, 'r')
    output = []
    # [(([{<{(<{{[({{}{}}{[]()})<{{}()}>]}}(([{{{}[]}[[]()]}[<{}[]]{()()}]](({{}{}}{{}()}))){[{({}())[[
    for line in f:
        output.append(list(line.strip()))
    
    return output


if '__main__' in __name__:
    main()
