# Definition for singly-linked list.
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list.
#  The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val > list2.val:
            head = list2
            head.next = self.mergeTwoLists(list1, list2.next)
        else:
            head = list1
            head.next = self.mergeTwoLists(list1.next, list2)

        return head


# recursively
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
