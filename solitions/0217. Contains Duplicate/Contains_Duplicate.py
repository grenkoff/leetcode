# https://leetcode.com/problems/contains-duplicate/

class Solution:
    # One Liner Brute Force
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     return len(set(nums)) != len(nums)

    
    # Time: O(n), Space: O(n)
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


a = Solution()

print(a.containsDuplicate([1, 2, 3, 1]))
print(a.containsDuplicate([1, 2, 3, 4]))
