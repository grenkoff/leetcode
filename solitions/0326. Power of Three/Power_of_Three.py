# https://leetcode.com/problems/power-of-three/

class Solution:
    # Recursive Solution
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n % 3 != 0 and n != 1:
            return False
        if n == 3 or n == 1:
            return True
        return self.isPowerOfThree(n // 3)
    
    # Math Solution
    def mathSolution(self, n: int) -> bool:
        return n > 0 and (math.log10(n) / math.log10(3)) % 1 == 0
    
    # Loop Solution
    def loopSolution(self, n: int) -> bool:
        if n < 1:
            return False
        while(n % 3 == 0):
            n /= 3
        return n == 1
