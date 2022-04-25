Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # neetcode https://www.youtube.com/watch?v=G0_I-ZF0S38
        if head is None:
            return head
        NewHead = head
        if head.next:
            NewHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return NewHead
    
    
    def reverse(self, head):
        # https://www.interviewbit.com/blog/reverse-a-linked-list/
        # The recursive approach to reverse a linked list is simple,
        #  just we have to divide the linked lists in two parts and
        #  i.e first node and the rest of the linked list, 
        # and then call the recursion for the other part by maintaining the connection.
        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head
 
        # Reverse the rest list
        rest = self.reverse(head.next)
 
        # Put first element at the end
        head.next.next = head
        head.next = None
 
        # Fix the header pointer
        return rest
    
    def reverseList(self, head):
        # По порядку от первой к последней
        # https://leetcode.com/problems/reverse-linked-list/discuss/58127/Python-Iterative-and-Recursive-Solution
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        # 
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)