from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    phone = [['0'],['1'],["A","B","C"], ["D","E","F"],["G","H","I"],["J","K","L"],["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","X","Y","Z"]]
    result = set()
    def generate(i, path):
        if len(path) == len(phone_number):
            result.add("".join(path))
            return
        if i >= len(phone_number):
            return

        for char in phone[int(phone_number[i])]:
            path.append(char)
            generate(i+1, path)
            path.pop()
            
    generate(0, [])
    return list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
