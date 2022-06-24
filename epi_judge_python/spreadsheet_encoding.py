from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    base = 0
    value = 0
    for char in reversed(col):
        val = ord(char) - ord('A') + 1
        value += val*(26**base)
        base+=1
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
