# https://leetcode.com/problems/permutations/
# https://leetcode.com/problems/permutations/solutions/2074177/Mathematical-proof-that-time-complexity-is-O(e-*-n!)-NOT-O(n-*-n/
# https://leetcode.com/problems/permutations/solutions/551252/short-recursive-python-solution/
# https://leetcode.com/problems/permutations/solutions/18241/one-liners-in-python/

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
    def withBacktracking(self, nums):
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

    
    # Recursive without backtracking (implicit stack)
    # Time: O(n!), Space: O(n!)
    # Approach 2 --> https://leetcode.com/problems/permutations/solutions/993970/python-4-approaches-visuals-time-complexity-analysis/
    
    
    # DFS Iterative with Explicit Stack
    # Time: O(n!), Space: O(n!)
    def dfs(self, nums):
        stack = [(nums, [])]
        res = []
        while stack:
            nums, path = stack.pop()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                stack.append((newNums, path+[nums[i]]))
        return res
    
    
    # BFS Iterative with a queue
    # Time: O(n!), Space: O(n!)
    def bfs(self, nums):
        from collections import deque
        q = deque()
        q.append((nums, []))  # -- nums, path (or perms)
        res = []
        while q:
            nums, path = q.popleft()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                q.append((newNums, path+[nums[i]]))
        return res
