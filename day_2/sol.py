import sys
import os
import typing

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.reader import read_lines
from tools.test_utils import shouldBeEqual

def isInvalid(product_id, nb_group=2) :
    product_id_str = str(product_id)
    if len(product_id_str) % nb_group != 0 :
        return 0
    len1Group = len(product_id_str) // nb_group
    pattern = product_id_str[:len1Group]
    ans = 0
    if all( pattern == product_id_str[i : i+len1Group] for i in range(len1Group, len(product_id_str), len1Group)) :
        # print(product_id_str, pattern, [product_id_str[i : i+len1Group] for i in range(len1Group, len(product_id_str), len1Group)])
        # print(ans)
        return True
    return False

def solve(is_part1 = True, fileName: str = ''):
    input_path = os.path.join(os.path.dirname(__file__), fileName)
    ans = 0
    for line in read_lines(input_path):
        for interval in line.split(","):
            start, end = interval.split('-')
            for product_id in range(int(start), int(end)+1) :
                if is_part1:
                    if isInvalid(product_id) :
                        ans += product_id
                else :
                    if any(isInvalid(product_id, nb_group) for nb_group in range(2, len(str(product_id)) + 1)) :
                        ans += product_id
    return ans

if __name__ == "__main__":

    shouldBeEqual(solve, {"is_part1": True, "fileName": 'test_input.txt'}, 1227775554)
    shouldBeEqual(solve, {"is_part1": True, "fileName": 'real_input.txt'}, 40398804950)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'test_input.txt'}, 4174379265)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'real_input.txt'}, 65794984339)