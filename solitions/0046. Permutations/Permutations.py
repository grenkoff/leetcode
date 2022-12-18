# https://leetcode.com/problems/permutations/

class Solution:
    # Iterative Solution
    # Time: O(?), Space: O(?)
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]   
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):   
                    new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
        return perms
    
    # Recursive with backtracking (implicit stack)
    # Time: O(n!), Space: O(n!)
    def permute(self, nums):
        def recursive(nums, perm=[], res=[]):
            if not nums:
                res.append(perm[::])
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                perm.append(nums[i])
                recursive(newNums, perm, res)
                perm.pop()
            return res
        return recursive(nums)
