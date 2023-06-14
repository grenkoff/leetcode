# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    # Time: O(n)
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest


a = Solution()

print(a.longestConsecutive([100,4,200,1,3,2])) # 4
print(a.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
