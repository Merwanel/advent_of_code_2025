import sys
import os
import typing

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.reader import read_lines
from tools.test_utils import shouldBeEqual


def solve(is_part1 = True, fileName: str = ''):
    input_path = os.path.join(os.path.dirname(__file__), fileName)
    ans = 0
    for line in read_lines(input_path):
        def greedy(i : int, remaining_ : int) -> str :
            if remaining_ == 0 :
                return ""
            highest_i = i
            for j in range(i, len(line) + 1 - remaining_) :
                if line[highest_i] < line[j] :
                    highest_i = j
            return line[highest_i] + greedy(highest_i+1, remaining_-1)
        if is_part1 :
            ans += int(greedy(0, 2))
        else :
            ans += int(greedy(0, 12))
    return ans

if __name__ == "__main__":

    shouldBeEqual(solve, {"is_part1": True, "fileName": 'test_input.txt'}, 357)
    shouldBeEqual(solve, {"is_part1": True, "fileName": 'real_input.txt'}, 17524)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'test_input.txt'}, 3121910778619)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'real_input.txt'}, 173848577117276)