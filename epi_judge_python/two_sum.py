from typing import List
 
from test_framework import generic_test


def has_two_sum(A: List[int], t: int) -> bool:
    there = {}
    count = 0
    for num in A:
        if t-num in there or t-num == num:
            return True  
        there[num] = 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                       has_two_sum))
