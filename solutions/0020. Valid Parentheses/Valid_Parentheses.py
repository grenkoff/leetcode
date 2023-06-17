# https://leetcode.com/problems/valid-parentheses/

class Solution:
    # Stack-based solution
    # Time: O(n), Space: O(n)
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack


a = Solution()

print(a.isValid("()")) # True
print(a.isValid("()[]{}")) # True
print(a.isValid("(]")) # False
