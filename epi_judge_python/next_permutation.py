from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    k = len(perm) - 2
    while k>=0 and perm[k] >= perm[k+1]:
        k-=1
    if k == -1:
        return []

    for i in range(len(perm)-1, k-1, -1):
        if perm[i] > perm[k]:
            perm[i], perm[k] = perm[k], perm[i]
            break

    perm[k+1:] = reversed(perm[k+1:])
    return perm

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
