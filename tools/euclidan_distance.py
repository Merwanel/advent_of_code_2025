import math
from typing import List

def euclidianDistance(coords1 : List[int], coords2: List[int]) :
    return math.sqrt(sum( (c1 - c2) ** 2 for c1, c2 in zip(coords1, coords2)))