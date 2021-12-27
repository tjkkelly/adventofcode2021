#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

from typing import List

def main():
    score_mapping = {']': 57, '}': 1197, ')': 3, '>': 25137}

    chunks = process_input('input.txt')
    scores = []
    for chunk in chunks:
        is_incomp, stack = is_incomplete(chunk)
        if is_incomp:
            scores.append(score(stack))

    scores = sorted(scores)
    middle = int(len(scores) / 2)
    print(scores[middle])
    

def score(stack):
    mapping = {'[': 2, '{': 3, '(': 1, '<': 4}
    score = 0
    for val in reversed(stack):
        score *= 5
        score += mapping[val]
    return score


def is_incomplete(chunk):
    mapping = {']':'[', '}':'{', ')':'(', '>':'<'}
    stack = []
    for val in chunk:
        if val in mapping.values():
            stack.append(val)
        else:
            if len(stack) == 0 or mapping[val] != stack[-1]:
                return False, None
            else:
                stack.pop()

    return True, stack

  
def process_input(fileName : str):
    f = open(fileName, 'r')
    output = []
    # [(([{<{(<{{[({{}{}}{[]()})<{{}()}>]}}(([{{{}[]}[[]()]}[<{}[]]{()()}]](({{}{}}{{}()}))){[{({}())[[
    for line in f:
        output.append(list(line.strip()))
    
    return output


if '__main__' in __name__:
    main()
