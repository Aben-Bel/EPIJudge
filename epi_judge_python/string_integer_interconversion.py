from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    sign = 1
    if x < 0:
        sign = -1
        x = x*(-1)
    res = ""
    while x > 0:
        res = str(x%10) + res
        x//=10
    if res == "":
        res = "0"
    return res if sign == 1 else "-"+res


def string_to_int(s: str) -> int:
    sign = 1
    if s[0] == "-":
        sign = -1
        s = s[1:]
    if s[0] == "+":
        s = s[1:]
    res = 0
    # 123 
    for char in s:
        res = res + int(char) 
        res *= 10
    
    return (res//10)*sign

# print("ans:", string_to_int('0'))
def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
