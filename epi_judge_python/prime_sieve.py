from cmath import sqrt
from math import ceil
from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    primes = []
    isPrime = [False,False] + [True]*(n-1)
    for i in range(n+1):
        if isPrime[i]:
            primes.append(i)

            for j in range(i,n+1,i):
                isPrime[j] = False
    return primes

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
