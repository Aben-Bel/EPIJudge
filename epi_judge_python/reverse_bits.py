from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    i = 63
    res = 0
    while i>=0:
        val = ((x>>i)&1)
        if val == 1:
            res = res | 1<<(63-i)
        i -= 1
        # j += 1 
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
