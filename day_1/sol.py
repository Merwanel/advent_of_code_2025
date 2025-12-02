import sys
import os
import typing

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.reader import read_lines
from tools.test_utils import shouldBeEqual

def solve(is_part1 = True, fileName: str = ''):
    input_path = os.path.join(os.path.dirname(__file__), fileName)
    cur = 50
    ans = 0
    for line in read_lines(input_path):
        direction, steps = line[0], int(line[1:])
        prev = cur
        
        if direction == "R":
            if not is_part1:
                ans += (prev + steps) // 100 - prev // 100
            cur = (cur + steps) % 100
        else: # "L"
            if not is_part1:
                ans += (prev - 1) // 100 - (prev - steps - 1) // 100
            cur = (cur - steps) % 100

        if is_part1:
            ans += cur == 0
            
    return ans

if __name__ == "__main__":

    shouldBeEqual(solve, {"is_part1": True, "fileName": 'test_input.txt'}, 3)
    shouldBeEqual(solve, {"is_part1": True, "fileName": 'real_input.txt'}, 1011)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'test_input.txt'}, 6)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'real_input.txt'}, 5937)