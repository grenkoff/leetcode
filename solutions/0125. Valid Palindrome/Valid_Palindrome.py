# https://leetcode.com/problems/valid-palindrome/

class Solution:
    # Time: O(n)
    # def isPalindrome(self, s: str) -> bool:
    #     lowercase = ""
    #     for char in s:
    #         if char.isalnum():
    #             lowercase += char.lower()
    #     return lowercase == lowercase[::-1]

    # Two Pointers Solution
    # Time: O(n), Space: O(1)
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not self.alphanum(s[l]):
                l += 1
                continue
            if not self.alphanum(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return "A" <= c <= "Z" or "a" <= c <= "z" or "0" <= c <= "9"
    

a = Solution()

print(a.isPalindrome("A man, a plan, a canal: Panama")) # True
print(a.isPalindrome("race a car")) # False
print(a.isPalindrome(" ")) # True
