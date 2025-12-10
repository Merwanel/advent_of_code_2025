import sys
import os
import typing
import collections

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.reader import read_lines
from tools.test_utils import shouldBeEqual
from tools.euclidan_distance import euclidianDistance
from tools.union_find import UnionFind


def solve(is_part1 = True, fileName: str = '', nb_junction=10):
    input_path = os.path.join(os.path.dirname(__file__), fileName)
    points = []
    for line in read_lines(input_path):
        points.append(list(map(int, line.split(","))))
    distances_sorted = sorted((euclidianDistance(points[i1], points[i2]), i1, i2) for i1 in range(len(points)) for i2 in range(i1+1, len(points)))

    uf = UnionFind(len(points))
    for i in range(nb_junction) :
        _, i1, i2 = distances_sorted[i]
        uf.union(i1, i2)
    if is_part1 :
        component_sizes = sorted(uf.get_componnent_size().values(), reverse=True)
        return component_sizes[0] * component_sizes[1] * component_sizes[2]
    
    last_i1, last_i2 = -1, -1 
    i = 11
    while uf.get_nb_componnents() > 1 :
        _, i1, i2 = distances_sorted[i]
        last_i1, last_i2 = i1, i2
        uf.union(i1, i2)
        i += 1
    x1, x2 = points[last_i1][0] , points[last_i2][0]

    return x1 * x2


if __name__ == "__main__":

    shouldBeEqual(solve, {"is_part1": True, "fileName": 'test_input.txt'}, 40)
    shouldBeEqual(solve, {"is_part1": True, "fileName": 'real_input.txt', 'nb_junction': 1000}, 90036)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'test_input.txt'}, 25272)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'real_input.txt'}, 6083499488)  
