# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    # Brute Force
    # Time: O(n * n), Space: O(1)
    def bruteForce(self, s: str) -> int:
        for i in range(len(s)):
                if s.count(s[i]) == 1:
                    return i
        return -1
    
    # Using HashMap and enumerate()
    # Time: O(n), Space: O(1)
    def hashMap(self, s: str) -> int:
        str_dict = {}
        for i in s:
            if i in str_dict:
                str_dict[i] += 1
            else:
                str_dict[i] = 1
        for idx, ch in enumerate(s):
            if str_dict[ch] == 1:
                return idx
        return -1
        
    # Pythonic Approach using collections.Counter()
    # Time: O(n), Space: O(1)
    def usingCounter(self, s: str) -> int:
        for a, b in Counter(s).items():
            if b == 1:
                return s.index(a)
        return -1
    
    # Fastest Approach using find() & rfind()
    # Time: O(n), Space: O(1)
    def usingRfind(self, s: str) -> int:
        abc = "abcdefghijklmnopqrstuvwxyz"
        res = 10 ** 5
        for c in abc:
            idx = s.find(c)
            if (idx != -1 and idx == s.rfind(c)):
                res = min(res, idx)
        return res if res < 10**5 else -1
