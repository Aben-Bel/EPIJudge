from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    dictionary = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
    integer = 0
    i=0
    while i<len(s):
        if i+1<len(s) and dictionary[s[i]] < dictionary[s[i+1]]:
            integer += -dictionary[s[i]]
            i+=1
        else:
            integer += dictionary[s[i]]
            i+=1
    return integer
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
