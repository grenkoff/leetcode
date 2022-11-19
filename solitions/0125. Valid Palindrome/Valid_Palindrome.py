# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for x in [*s]:
            if x.isalpha(): a += x.lower()
            if x.isnumeric(): a += x
        return a == a[::-1]
