from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    res = 0
    # 31.0,31.5,275,295,260,270,290,230,255,250
    cur_min = prices[0]
    for stock in prices:
        if cur_min > stock:
            cur_min = stock
        res = max(res, stock - cur_min)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
