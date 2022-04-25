# TASK 
# Given a linked list, swap every two adjacent nodes and return its head.
#  You must solve the problem without modifying the values
#   in the list's nodes (i.e., only nodes themselves may be changed.)

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]


# SOLUTION 
#https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/discuss/477540/Python-Recursive-Solution-w-Step-by-Step-Thought-Process
# Is the point of Leetcode to come up with intensely technical and condensed code, or is it to help us practice systematically solving problems and showing our thought process? Its the latter. This may not be the most condensed solution, but the thought process is clear and sequential.

# Overall Thought Process

# Write out ideally how the algorithm would execute. It'll be easier to see the pattern this way
# Then, I look at pairs and try to come up with a pseudocode
# From that, I can come up with a rough recursive algorithm. To simplify this, I'm not thinking of edge cases
# Add in conditionals to account for edge cases
# Convert algorithm into code
# Walking through each Step

# 1. Write out ideally how the algorithm would execute. It'll be easier to see the pattern this way

# For linked list -> 1 - 2
# 2.next = 1
# 1.next = None
# return 2

# For linked list -> 1 - 2 - 3
# 2.next = 1
# 1.next = None
# return 2

# For linked list -> 1 - 2 - 3 - 4
# 4.next = 3
# 3.next = None
# 2.next = 1
# 1.next = 4
# return 2

# For linked list -> 1 - 2 - 3 - 4 - 5
# 4.next = 3
# 3.next = 5
# 2.next = 1
# 1.next = 4
# return 2
# 2. Then, I look at pairs and try to come up with a pseudocode

# for each pair (a, b):
#     a.next = whatever is the first of next pair
#     b.next = a
#     return b
# 3. From that, I can come up with a rough recursive algorithm. To simplify this, I'm not thinking of edge cases yet

# swap_pair(head):
#     first = head
#     second = first.next
    
#     first.next = swap_pair(second.next)
#     second.next = first
#     return second
# 4. Add in conditionals to account for edge cases

# swap_pair(head):
#     if not head:
#         return None

#     first = head
    
#     if not first.next:
#         return first
#     second = first.next
    
#     first.next = swap_pair(second.next)
#     second.next = first
#     return second
# 5. Convert algorithm into code

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None

        first = head
        if not first.next:
            return first
        second = first.next

        first.next = self.swapPairs(second.next)
        second.next = first
        return second