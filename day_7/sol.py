import sys
import os
import typing
import collections

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.reader import read_lines
from tools.test_utils import shouldBeEqual


def solve(is_part1 = True, fileName: str = ''):
    input_path = os.path.join(os.path.dirname(__file__), fileName)
    mat = []
    for line in read_lines(input_path):
        mat.append(line)
    N, M = len(mat), len(mat[0])
    r0, c0 = 0, 0
    for c in range(M) :
        if mat[0][c] == "S" :
            c0 = c
    beams = collections.deque([(r0, c0)])
    spliter_hit = set()
    new_mat = [list(r) for r in mat]
    nb_time_split = [[0] * M for _ in range(N)]
    nb_time_split[r0][c0] = 1 
    while beams :
        r, c = beams.popleft()
        r += 1
        if r == N :
            continue
        if new_mat[r][c] == "|" :
            continue
        if mat[r][c] != "^" :
            new_mat[r][c] = "|"
            nb_time_split[r][c]  += nb_time_split[r-1][c]
            beams.append((r, c))
            continue
        #"^"
        
        nb_time_split[r][c+1] += nb_time_split[r-1][c] 
        nb_time_split[r][c-1] += nb_time_split[r-1][c] 
        beams.append((r, c-1))
        beams.append((r, c+1))
        spliter_hit.add((r, c))
    # [print("".join(r)) for r in new_mat]
    # [print(r) for r in nb_time_split]
    if is_part1 :
        return len(spliter_hit)
    return sum(nb_time_split[-1])

if __name__ == "__main__":

    shouldBeEqual(solve, {"is_part1": True, "fileName": 'test_input.txt'}, 21)
    shouldBeEqual(solve, {"is_part1": True, "fileName": 'real_input.txt'}, 1541)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'test_input.txt'}, 40)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'real_input.txt'}, 80158285728929)  
