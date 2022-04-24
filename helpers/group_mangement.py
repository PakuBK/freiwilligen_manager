import random
import math
from models.datatypes import RegionGraph

def choose_random_and_pop(fw) -> tuple:
    data = fw.copy()
    idx = random.randint(0, len(data)-1)
    value = data.pop(idx)
    return (value, data)

def calculate_max_region_diff(target, other_regions):
    diffs = [math.fabs(target-region) for region in other_regions]
    max = 0
    for d in diffs:
        if d > max:
            max = d
    return max

