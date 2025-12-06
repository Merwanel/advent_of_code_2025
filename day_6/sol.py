import sys
import os
import typing

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.reader import read_lines
from tools.test_utils import shouldBeEqual

def part1(input_path) :
    mat = []
    for line in read_lines(input_path):
        mat.append(line.split())
    operators = mat.pop()
    N, M = len(mat), len(mat[0])
    for r in range(N) :
        for c in range(M) :
            mat[r][c] = int(mat[r][c])
    ans = 0
    for problem in range(M) :
        if operators[problem] == "+" :
            ans += sum(mat[i][problem] for i in range(N))
        if operators[problem] == "*" :
            res_here = 1
            for i in range(N) :
                res_here *= mat[i][problem]
            ans += res_here
    return ans, operators

def solve(is_part1 = True, fileName: str = ''):
    input_path = os.path.join(os.path.dirname(__file__), fileName)
    ans, operators = part1(input_path)
    if is_part1 :
        return ans
    mat = []
    for line in read_lines(input_path, False):
        mat.append(line)
    mat.pop()
    N, M = len(mat), len(mat[0])
    new_mat = [ [0] * N  for _ in range(M)]
    for r in range(N) :
        for c in range(M) :
            new_mat[c][r] = mat[r][c]
    N, M = len(new_mat), len(new_mat[0])
    problem = 0
    ans = 0
    res_here = 0 if operators[problem] == "+" else 1
    for r in range(N) :
        joined = "".join(new_mat[r]).strip().rstrip()
        if joined == "" :
            problem += 1
            ans += res_here
            res_here = 0 if problem < len(operators) and operators[problem] == "+" else 1
            continue
        num_here = int(joined)
        if operators[problem] == "+" :
            res_here += num_here
        else :
            res_here *= num_here

    ans += res_here
    return ans

    
    

    

if __name__ == "__main__":

    shouldBeEqual(solve, {"is_part1": True, "fileName": 'test_input.txt'}, 4277556)
    shouldBeEqual(solve, {"is_part1": True, "fileName": 'real_input.txt'}, 4405895212738)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'test_input.txt'}, 3263827)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'real_input.txt'}, 7450962489289)  
