import sys
import os
import typing

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.reader import read_lines
from tools.test_utils import shouldBeEqual


def solve(is_part1 = True, fileName: str = ''):
    input_path = os.path.join(os.path.dirname(__file__), fileName)
    intervals = []
    are_ranges_done = False
    cpt = 0
    for line in read_lines(input_path):
        if line == "" :
            are_ranges_done = True
            continue
        if are_ranges_done :
            ingredient = int(line)
            cpt += any( start <= ingredient <= end for start, end in intervals)
        else :
            start, end = line.split('-')
            intervals.append((int(start), int(end)))
    if is_part1 :
        return cpt
    
    events = []
    IS_START = False
    for start, end in intervals :
        events.append((start, IS_START))
        events.append((end, not IS_START))

    events.sort()
    balance = 0
    tmp = set()
    prev = events[0][0]+1
    cpt_part2 = 0
    new_intervals = []
    new_start = None
    for cur, is_start in events :
        if is_start == IS_START :
            balance += 1
        else :
            balance -= 1
        if balance > 0 :
            cpt_part2 += cur - prev - 1
        tmp.add(cur)
        prev = cur

        if balance > 0 :
            if new_start == None :
                new_start = cur
        else :
            new_intervals.append((new_start, cur))
            new_start = None

    return sum( end - start + 1 for start, end in new_intervals)
    

    

if __name__ == "__main__":

    shouldBeEqual(solve, {"is_part1": True, "fileName": 'test_input.txt'}, 3)
    shouldBeEqual(solve, {"is_part1": True, "fileName": 'real_input.txt'}, 775)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'test_input.txt'}, 14)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'real_input.txt'}, 350684792662845)  
