# https://leetcode.com/problems/contains-duplicate/

class Solution:
    # One Liner Brute Force
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
