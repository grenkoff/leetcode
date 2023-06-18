# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack-based solution
        # Time: O(n), Space: O(n)
        stack = []
        hashmap = {')':'(', '}':'{', ']':'['}

        for p in s:
            if p in hashmap.values():
                stack.append(p)
            elif stack and hashmap[p] == stack[-1]:
                stack.pop()
            else:
                return False

        return stack == []


a = Solution()

print(a.isValid("()")) # True
print(a.isValid("()[]{}")) # True
print(a.isValid("([{}])")) # True
print(a.isValid("[([]){}]")) # True
print(a.isValid("(]")) # False
