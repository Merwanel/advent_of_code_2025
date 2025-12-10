from typing import List, Set
from collections import deque

def floodFill(mat: List[List[str]], out_symbols: List[str], in_symbols: List[str], fill_char: str) -> None:
    if not mat or not mat[0]:
        return

    rows = len(mat)
    cols = len(mat[0])
    
    valid_symbols = out_symbols + in_symbols
    out_set = set(out_symbols)
    
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] not in valid_symbols:
                raise ValueError(f"Unknown symbol '{mat[r][c]}' at ({r}, {c})")
    
    visited = set()
    queue = deque([(0, 0)])
    visited.add((0, 0))
    
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r2, c2 = r + dr, c + dc
            
            if 0 <= r2 < rows + 2 and 0 <= c2 < cols + 2:
                if (r2, c2) not in visited:
                    is_traversable = False
                    
                    if r2 == 0 or r2 == rows + 1 or c2 == 0 or c2 == cols + 1:
                        is_traversable = True
                    else:
                        real_r, real_c = r2 - 1, c2 - 1
                        if mat[real_r][real_c] in out_set:
                            is_traversable = True
                            
                    if is_traversable:
                        visited.add((r2, c2))
                        queue.append((r2, c2))
                        
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] in out_set:
                if (r + 1, c + 1) not in visited:
                    mat[r][c] = fill_char
