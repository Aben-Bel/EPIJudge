from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    # 2,0,1,3
    # a,b,c,d
    res = [""]*len(A)
    for i in range(len(perm)):
        res[perm[i]] = A[i]
    A[:] = res
    

    


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
