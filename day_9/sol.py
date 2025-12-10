from collections import defaultdict
import sys
import os
import typing
import collections

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.reader import read_lines
from tools.test_utils import shouldBeEqual
from tools.flood_fill import floodFill
from tools.matrix_utils import build_2d_prefix_sum, query_2d_prefix_sum


def solve(is_part1 = True, fileName: str = ''):
    input_path = os.path.join(os.path.dirname(__file__), fileName)
    reds = []
    for line in read_lines(input_path):
        y, x = line.split(',')
        reds.append((int(x), int(y)))
    R = len(reds)
    sorted_x, sorted_y = sorted(set(x for x, _ in reds)), sorted(set(y for _, y in reds))
    big_to_small_x = {}
    small_to_big_x = {}
    cur_x = 0
    for x in sorted_x :
        big_to_small_x[x] = cur_x
        small_to_big_x[cur_x] = x
        cur_x += 1
    big_to_small_y = {}
    small_to_big_y = {}
    cur_y = 0
    for y in sorted_y :
        big_to_small_y[y] = cur_y
        small_to_big_y[cur_y] = y
        cur_y += 1
    small_reds = [(big_to_small_x[x], big_to_small_y[y]) for x, y in reds]
    if is_part1 : 
        biggest = 0
        for i in range(R) :
            xi, yi = small_reds[i]
            xi_big = small_to_big_x[xi]
            yi_big = small_to_big_y[yi]
            for j in range(i+1, R) :
                xj, yj = small_reds[j]
                xj_big = small_to_big_x[xj]
                yj_big = small_to_big_y[yj]
                cur_area = (abs(yj_big - yi_big) + 1) * (abs(xi_big - xj_big) + 1) 
                biggest = max(biggest, cur_area)
        return biggest
    N, M = max(x for x, _ in small_reds) + 1 , max( y for _ , y in small_reds) + 1
    mat = [["."] * M for _ in range(N)]
    for x, y in small_reds :
        mat[x][y] = "#"
    horizontals = defaultdict(list)
    verticals = defaultdict(list)
    for x, y in small_reds :
        horizontals[x].append(y)
        verticals[y].append(x)
    for x in horizontals :
        horizontals[x].sort()
        if  len(horizontals[x]) >= 2 :
            horizontals[x] = [horizontals[x][0]] + [horizontals[x][1]]
    for y in verticals :
        verticals[y].sort()
        if  len(verticals[y]) >= 2 :
            verticals[y] = [verticals[y][0]] + [verticals[y][1]]

    for x in horizontals :
        if len(horizontals[x]) == 1 : 
            continue
        y1, y2 = horizontals[x]
        for yk in range(y1, y2 + 1) :
            if mat[x][yk] == '.' : 
                mat[x][yk] = 'X'
            
    for y in verticals :
        if len(verticals[y]) == 1 : 
            continue
        x1, x2 = verticals[y]
        for xk in range(x1, x2 + 1) :
            if mat[xk][y] == ".": 
                mat[xk][y] = 'X'
    

    floodFill(mat, out_symbols=['.'], in_symbols=['X', '#'], fill_char='X')
    

    bad_grid = [[1 if c == '.' else 0 for c in r] for r in mat]
    pref = build_2d_prefix_sum(bad_grid)

    biggest = 0
    for i1 in range(len(small_reds)) :
        x1, y1 = small_reds[i1]
        for i2 in range(i1 + 1, len(small_reds)) :
            x2, y2 = small_reds[i2]
            
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            

            if query_2d_prefix_sum(pref, min_x, min_y, max_x, max_y) == 0:
                x1_big = small_to_big_x[x1]
                y1_big = small_to_big_y[y1]
                x2_big = small_to_big_x[x2]
                y2_big = small_to_big_y[y2]
                cur_area = (abs(y2_big - y1_big) + 1) * (abs(x2_big - x1_big) + 1) 
                biggest = max(biggest, cur_area)
    
    return biggest

if __name__ == "__main__":

    shouldBeEqual(solve, {"is_part1": True, "fileName": 'test_input.txt'}, 50)
    shouldBeEqual(solve, {"is_part1": True, "fileName": 'real_input.txt'}, 4774877510)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'test_input.txt'}, 24)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'real_input.txt'}, 1560475800)  
