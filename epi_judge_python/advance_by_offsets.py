from functools import lru_cache
from typing import List

from test_framework import generic_test




def can_reach_end(A: List[int]) -> bool:
    furthest = 0
    i = 0 
    while i<=furthest and i<len(A)-1:
        furthest = max(furthest, A[i]+i)
        i+=1
    return furthest >= len(A)-1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
