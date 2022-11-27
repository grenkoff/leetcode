# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Using List :: Time: O(n ** 2), Space: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        while head:
            if head in seen:
                return True
            seen.append(head)
            head = head.next 
        return False
    
    # Using Set :: Time: O(n), Space: O(n)
    def hashSet(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
    
    # Two Pointers :: Time: O(n), Space: O(1)
    def twoPointers(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
