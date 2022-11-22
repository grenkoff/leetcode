# https://leetcode.com/problems/sqrtx/

# Binary Search. O(log n)
class Solution:
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