# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    # 1st method
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res
    
    # 2nd method
    def secondMethod(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res
