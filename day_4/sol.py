import sys
import os
import typing

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.reader import read_lines
from tools.test_utils import shouldBeEqual


def isCellAccessible(mat, r, c) :
    if mat[r][c] == "." :
        return True
    N, M = len(mat), len(mat[0])
    cpt_paper_around = 0 
    if r - 1 >= 0 and mat[r-1][c] == "@" :  # top
        cpt_paper_around += 1
    if r - 1 >= 0 and c - 1 >= 0 and mat[r-1][c-1] == "@" :  # top-left
        cpt_paper_around += 1
    if c - 1 >= 0 and mat[r][c-1] == "@" :  # left
        cpt_paper_around += 1
    if r + 1 < N and c - 1 >= 0 and mat[r+1][c-1] == "@" :  # bottom-left
        cpt_paper_around += 1
    if r + 1 < N and mat[r+1][c] == "@" :  # bottom
        cpt_paper_around += 1
    if r + 1 < N and c + 1 < M and mat[r+1][c+1] == "@" :  # bottom-right
        cpt_paper_around += 1
    if c + 1 < M and mat[r][c+1] == "@" :  # right
        cpt_paper_around += 1
    if  r - 1 >= 0 and c + 1 < M and mat[r-1][c+1] == "@" :  # top-right
        cpt_paper_around += 1
    return cpt_paper_around < 4

def findRemovable_mat(mat) :
    new_mat = [list(r) for r in mat]
    N, M = len(mat), len(mat[0])
    for r in range(N) :
        for c in range(M) :
            if mat[r][c] != "@" :
                continue
            if isCellAccessible(mat, r, c)  :
                new_mat[r][c] = 'X'
    return new_mat

def solve(is_part1 = True, fileName: str = ''):
    input_path = os.path.join(os.path.dirname(__file__), fileName)
    mat = []
    for line in read_lines(input_path):
        mat.append(line)
    cpt_removable = 0
    mat = findRemovable_mat(mat)
    N, M = len(mat), len(mat[0])
    if is_part1 :
        return sum( mat[r].count("X") for r in range(N) )
    cpt_accessible = 0
    foundSomeAccessible = True
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    # print(cpt_accessible, sum( mat[r].count("X") for r in range(N) ))
    # print("\n".join(["".join(r) for r in mat]))
    k=0
    while foundSomeAccessible :
        k += 1
        foundSomeAccessible = False
        bfs_queue = []
        seen = set()
        for r in range(N) :
            if mat[r][0] != "@" :
                bfs_queue.append((r, 0))
                seen.add((r, 0))
                if mat[r][0] == "X" : 
                    foundSomeAccessible = True
                    mat[r][0] = "."
                    cpt_accessible += 1
            if mat[r][M-1] != "@" :
                bfs_queue.append((r, M-1))
                seen.add((r, M-1))
                if mat[r][M-1] == "X" : 
                    foundSomeAccessible = True
                    mat[r][M-1] = "."
                    cpt_accessible += 1
        for c in range(1,M-1) :
            if mat[0][c] != "@" :
                bfs_queue.append((0, c))
                seen.add((0, c))
                if mat[0][c] == "X" : 
                    foundSomeAccessible = True
                    mat[0][c] = "."
                    cpt_accessible += 1
            if mat[N-1][c] != "@" :
                bfs_queue.append((N-1, c))
                seen.add((N-1, c))
                if mat[N-1][c] == "X" : 
                    foundSomeAccessible = True
                    mat[N-1][c] = "."
                    cpt_accessible += 1
        while len(bfs_queue) > 0 :
            r, c = bfs_queue.pop(0)
            for dr, dc in DIRECTIONS :
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= M :
                    continue
                if (nr, nc) in seen :
                    continue
                if mat[nr][nc] != "@" :
                    if mat[nr][nc] == "X" :
                        mat[nr][nc] = "."
                        foundSomeAccessible = True
                        cpt_accessible += 1
                    seen.add((nr, nc))
                    bfs_queue.append((nr, nc))
        mat = findRemovable_mat(mat)
        # print()
        # print(foundSomeAccessible, k ,cpt_accessible, sum( mat[r].count("X") for r in range(N) ))
        # print("\n".join(["".join(r) for r in mat]))
    return cpt_accessible + sum( mat[r].count("X") for r in range(N) )
    

    

if __name__ == "__main__":

    shouldBeEqual(solve, {"is_part1": True, "fileName": 'test_input.txt'}, 13)
    shouldBeEqual(solve, {"is_part1": True, "fileName": 'real_input.txt'}, 1419)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'test_input.txt'}, 43)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'real_input.txt'}, 8739)