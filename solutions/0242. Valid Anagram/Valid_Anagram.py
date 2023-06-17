# https://leetcode.com/problems/valid-anagram/

class Solution:
    # Brute Force method
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t):


    # Approach using str.count()
    # Time: O(n)
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t): 
    #         return False
    #     letters = "abcdefghijklmnopqrstuvwxyz"
    #     for letter in letters:
    #         if s.count(letter) != t.count(letter):
    #             return False
    #     return True


    # Time: O(s+t)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)


        return count_s == count_t


a = Solution()

print(a.isAnagram("anagram", "nagaram")) # True
print(a.isAnagram("cat", "rat")) # False
