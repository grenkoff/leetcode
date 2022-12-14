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
