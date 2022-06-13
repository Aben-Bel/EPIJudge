from functools import lru_cache
from turtle import back
from typing import List

from test_framework import generic_test




def buy_and_sell_stock_twice(prices: List[float]) -> float:
    forward = [0]*(len(prices)+1)
    runningMinimum = float('inf')
    for i in range(1,len(prices)+1):
        if runningMinimum > prices[i-1]:
            runningMinimum = prices[i-1]
        forward[i] = max(prices[i-1] - runningMinimum, forward[i-1])
    backward = [0]*(len(prices)+1)
    
    runningMaximum = float('-inf')
    for i in range(len(prices)-1, -1, -1):
        if runningMaximum < prices[i]:
            runningMaximum = prices[i]
        backward[i] = max(runningMaximum - prices[i], backward[i+1])
    backward = backward[:len(backward)-1]
    forward = forward[1:] + [0]
    maxProfit = float('-inf')
    for i in range(len(forward)-1):
        maxProfit = max(maxProfit, forward[i-1]+backward[i])
    return maxProfit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
