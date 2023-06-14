#https://leetcode.com/problems/two-sum/

class Solution:
    # Time: O(n**2)
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]


    # HashMap Solution
    # Time: O(n), Space: O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        return


a = Solution()

print(a.twoSum([2, 1, 3, 4], 4)) # [1, 2]
print(a.twoSum([2, 7, 11, 15], 9)) # [0, 1]
