from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    result = []
    n = len(square_matrix)
    
    count = 0
    while count < len(result):
        for i in range(count, n-count):
            result.append(square_matrix[count][i])
        
        for i in range(count+1, n-count):
            result.append(square_matrix[i][n-count-1])
        
        for i in range(n-count-2, count-1,-1):
            result.append(square_matrix[n-count-1][i])
        
        for i in range(n-count-2, count,-1):
            result.append(square_matrix[i][count])
        count += 1
    return result
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
