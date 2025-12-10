from typing import List

def build_2d_prefix_sum(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    pref = [[0] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            val = matrix[r][c]
            top = pref[r-1][c] if r > 0 else 0
            left = pref[r][c-1] if c > 0 else 0
            top_left = pref[r-1][c-1] if (r > 0 and c > 0) else 0
            
            pref[r][c] = val + top + left - top_left
            
    return pref

def query_2d_prefix_sum(pref: List[List[int]], r1: int, c1: int, r2: int, c2: int) -> int:
    total = pref[r2][c2]
    top = pref[r1-1][c2] if r1 > 0 else 0
    left = pref[r2][c1-1] if c1 > 0 else 0
    top_left = pref[r1-1][c1-1] if (r1 > 0 and c1 > 0) else 0
    
    return total - top - left + top_left
