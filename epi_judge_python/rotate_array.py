import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def rotate_array(rotate_amount: int, A: List[int]) -> None:
    rotate_amount = rotate_amount % 4
    n = len(A)
    result = [[0 for i in range(n)] for j in range(n)]
    # print("Result: ", result)

    while rotate_amount > 0:
        for i in range(n):
            for j in range(n):
                result[j][n-i-1] = A[i][j]
        # print("Rotated: ", result)
        for i in range(n):
            for j in range(n):
                A[i][j] = result[i][j]
        # print("Copied to A: ", A)
        rotate_amount -= 1



@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rotate_array.py', 'rotate_array.tsv',
                                       rotate_array_wrapper))
