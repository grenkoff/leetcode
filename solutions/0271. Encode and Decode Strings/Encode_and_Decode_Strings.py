# https://leetcode.com/problems/encode-and-decode-strings/

class Solution:


    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    

    def decode(self, s: str) -> list[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

a = Solution()

print(a.encode(["I", "love", "my", "wife"])) # 1#I4#love2#my4#wife
print(a.decode(a.encode(["I", "love", "my", "wife"]))) # ['I', 'love', 'my', 'wife']
