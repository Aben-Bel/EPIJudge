import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    s[:] = s[::-1]
    j = 0
    for i in range(len(s)):
        if s[i] == " ":
            s[j:i] = s[j:i][::-1]
            j = i+1
    
    s[j:len(s)] = s[j:len(s)][::-1]
    # val = "".join(s)
    # li = val.split(" ")
    # li = li[::-1]
    # val = " ".join(li)
    # for i in range(len(s)):
    #     s[i] = val[i]
    # return

"Bob likes Alice"

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
