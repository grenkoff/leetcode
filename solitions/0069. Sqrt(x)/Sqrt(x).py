# https://leetcode.com/problems/sqrtx/

class Solution:
    # Iterative Binary Search
    # Time: O(logn), Space: O(1)
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 2, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    # Recursive Binary Search
    # Time: O(logn), Space: O(logn)
    
    
    # Newton-Raphson method (read more: https://leetcode.com/problems/sqrtx/discuss/2732386/O(1)-solution-in-python!(Newton-Raphson-method))
    # Time: O(1), Space: O(?)
    def newtonRaphson(self, x: int) -> int:
        ans = 1.0
        for i in range(20):
            ans = ans - (ans * ans - x)/(2 * ans)
        return int(ans)
