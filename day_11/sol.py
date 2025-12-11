import collections
import sys
import os
import typing

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.reader import read_lines
from tools.test_utils import shouldBeEqual


def solve(is_part1 = True, fileName: str = ''):
    input_path = os.path.join(os.path.dirname(__file__), fileName)
    graph = collections.defaultdict(list)
    for line in read_lines(input_path):
        start, neighbors = line.split(':')
        neighbors = neighbors.split(' ')[1:]
        graph[start] = neighbors
        
    def waysFromTo(start, end):
        memo = {}
        def dfs(node):
            if node == end:
                return 1
            if node in memo:
                return memo[node]
            
            total = 0
            for neighbor in graph[node]:
                total += dfs(neighbor)
            
            memo[node] = total
            return total
        
        return dfs(start)

    if is_part1:
        return waysFromTo("you", "out")

    return (waysFromTo("svr", "fft") * waysFromTo("fft", "dac") * waysFromTo("dac", "out") 
            + waysFromTo("svr", "dac") * waysFromTo("dac", "fft") * waysFromTo("fft", "out"))

if __name__ == "__main__":

    shouldBeEqual(solve, {"is_part1": True, "fileName": 'test_input.txt'}, 5)
    shouldBeEqual(solve, {"is_part1": True, "fileName": 'real_input.txt'}, 796)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'test_input_2.txt'}, 2)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'real_input.txt'}, 294053029111296)
