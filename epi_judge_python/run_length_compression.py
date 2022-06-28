from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    decoded = ""
    left = 0
    right = 0
    while left <= right:
        while right<len(s) and s[right].isdigit():
            right+=1
        if right >= len(s)or left >= len(s): 
            break
        decoded += (s[right]*int(s[left:right]))
        left = right+1
        right+=1
    return decoded


def encoding(s: str) -> str:
    encoded = ""
    left, right = 0, 0
    while left<=right:
        while right<len(s) and s[left]==s[right]:
            right+=1
        if left >= len(s): 
            break
        encoded += str(right-left) + s[left]
        left = right
    return encoded



def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
