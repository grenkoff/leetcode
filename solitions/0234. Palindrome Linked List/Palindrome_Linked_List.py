# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Array Solution :: Space: O(n)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True
    
    # Two Pointers Solution :: Space: O(1)
    def twoPointers(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    
    # Recursive Solution
    def recursiveSolution(self, head: Optional[ListNode]) -> bool:
        global front
        front = head

        def helper(back) -> bool:
            global front
            if not back:
                return True

            #let back pointer travel to the back of the list through recursion
            equal_so_far = helper(back.next)

            #check if front and back have the same value
            value_equal = (front.val == back.val)

            #when the function return, back is gradually moved toward head of the list
            #move front accordingly to compare their value
            front = front.next
            return equal_so_far and value_equal
        
        return helper(head)
