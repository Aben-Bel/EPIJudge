from typing import List

from test_framework import generic_test

def checkDups(li):
    dup = set()
    for ele in li:
        if ele in dup and ele!=0:
            return False
        dup.add(ele)
    return True

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    for row in partial_assignment:
        if checkDups(row) == False:
            return False

    
    for i in range(len(partial_assignment)):
        if checkDups([partial_assignment[j][i] for j in range(len(partial_assignment))]) == False:
            return False
        

    for i in range(3):
        [0,1,2]
        start = 3*i
        for j in range(3):
            [0,1,2]
            collect = []
            endCol = 3*j
            for k in range(start, start+3):
                for l in range(endCol, endCol+3):
                    collect.append(partial_assignment[k][l])
            if checkDups(collect) == False:
                return False


    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
