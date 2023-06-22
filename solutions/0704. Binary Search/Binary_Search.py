# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Time: O(log n)
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


a = Solution()

assert a.search([-1,0,3,5,9,12], 9) == 4
assert a.search([-1,0,3,5,9,12], 2) == -1
