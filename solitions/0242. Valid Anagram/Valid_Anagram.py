# https://leetcode.com/problems/valid-anagram/

# Brute Force method
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

# Approach using str.count()
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = True
        if len(s) != len(t): 
            flag = False
        else:
            letters = "abcdefghijklmnopqrstuvwxyz"
            for letter in letters:
                if s.count(letter) != t.count(letter):
                    flag = False
                    break
        return flag
