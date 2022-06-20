from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    result = []
    n = len(square_matrix)

    urul = 0
    uldl = 0
    dldr = 0
    dlur = 0
    while n*n > len(result):
        for i in range(urul, n-urul):
            result.append(square_matrix[urul][i])
        urul += 1
        
        for i in range(uldl+1, n-uldl):
            result.append(square_matrix[i][n-uldl-1])
        uldl += 1
        
        for i in range(n-dldr-2, dldr-1,-1):
            result.append(square_matrix[n-dlur-1][i])
        dldr += 1
        
        for i in range(n-dlur-2, dlur,-1):
            result.append(square_matrix[i][dlur])
        dlur += 1
    return result
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
