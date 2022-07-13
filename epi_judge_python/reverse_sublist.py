from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummy= sub = ListNode(0, L)
    for _ in range(1, start):
        sub = sub.next
    
    first = sub.next
    for _ in range(finish-start):
        second = first.next
        first.next, second.next, sub.next = second.next, sub.next, second
    
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
