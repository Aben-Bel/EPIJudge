import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    end = len(s)-1
    start = size-1
    
    while start >= 0:
        if s[start] == "a":
            s[end] = "d"
            s[end-1]= "d"
            end -= 2
        elif s[start] != "b":
            s[end] = s[start]
            end-=1
        start -= 1

    return end


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
