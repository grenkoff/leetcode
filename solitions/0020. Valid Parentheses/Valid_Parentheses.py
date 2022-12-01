# https://leetcode.com/problems/valid-parentheses/

class Solution:
    # Stack-based solution
    # Time: O(n), Space: O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}
        for p in s:
            if p in closeToOpen.values():
                stack.append(p)
            elif stack and closeToOpen[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
