# https://leetcode.com/problems/reverse-string/

class Solution:
    # One-Liner Pythonic Approach
    def oneLiner(self, s: List[str]) -> None:
        return s.reverse()
    
    # Recursive Call Solution
    # Time: O(n), Space: O(n)
    
    # Stack-based Solution
    # Time: O(n), Space: O(n)
    
    # Two Pointers Approach
    # Time: O(n), Space: O(1)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
