from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    carry = 1
    for i in range(len(A)-1, -1, -1):
        if A[i] + carry > 9:
            A[i] = 0
            carry = 1
        else:
            A[i] += carry
            carry = 0
            break
    return A if carry == 0 else [carry] + A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
