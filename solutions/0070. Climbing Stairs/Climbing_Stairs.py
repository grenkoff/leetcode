# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = []
        for i in range(n):
            if i <= 2:
                f = 1
            else:
                f = dp[i-1] + dp[i-2]
                fib[i] = f
        return dp[i]
