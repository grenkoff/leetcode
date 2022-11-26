# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Two Pointers Time: O(n + m), Space: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
    
    # Hashset Time: O(n + m), Space: O(n)
    def hashSet(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first_set = set()
        curr = headA
        while curr:
            first_set.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in first_set:
                return curr
            curr = curr.next
        return None
