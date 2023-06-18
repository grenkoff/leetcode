# https://leetcode.com/problems/container-with-most-water/

class Solution:
    # Two Pointers Solution
    # Time: O(n)
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        h = max(height)

        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
            if (r - l) * h <= max_area:
                break 
        return max_area


a = Solution()

print(a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])) # 49
print(a.maxArea([1,1])) # 1
print(a.maxArea([3, 2, 101])) # 6
