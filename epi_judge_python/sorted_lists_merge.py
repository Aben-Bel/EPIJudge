from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = save = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            dummy.next = L1
            dummy = dummy.next
            L1 = L1.next
        else:
            dummy.next = L2
            dummy = dummy.next
            L2 = L2.next
    while L1:
        dummy.next = L1
        dummy = dummy.next
        L1 = L1.next
    
    while L2:
        dummy.next = L2
        dummy = dummy.next
        L2 = L2.next
    
    return save.next
            



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
