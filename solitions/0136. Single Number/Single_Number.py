# https://leetcode.com/problems/single-number/

class Solution:
    # Brute Force
    def bruteForce(self, nums: List[int]) -> int:
        return sum(list(set(nums)) * 2) - sum(nums)
    
    # Use Sorting
    def sorting(self, nums: List[int]) -> int:
        nums.sort()
        stack=[]
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] not  in stack :
                stack.append(nums[i])
            else:
                stack.pop()
        return stack[0]
    
    # Use Hashing/Set
    def hashing(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                del counts[i]
        return list(counts.keys())[0]
    
    # Bit Manipulation
    def bitManipulation(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
