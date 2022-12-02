# https://leetcode.com/problems/valid-anagram/

class Solution:
    # Brute Force method
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False


    # Approach using str.count()
    # Time: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            if s.count(letter) != t.count(letter):
                return False
        return True
