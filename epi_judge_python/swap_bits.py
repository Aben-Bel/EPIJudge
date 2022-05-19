from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    ith = (x>>i) & 1
    jth = (x>>j) & 1

    if ith != jth:
        x = x ^ (1<<i)
        x = x ^ (1<<j)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
