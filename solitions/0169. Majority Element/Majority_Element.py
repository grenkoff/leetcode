# https://leetcode.com/problems/majority-element/

class Solution:
    # Brute Force: Time O(n ** 2), Space O(1)
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num
    
    # HashMap: Time O(n), Space O(n)
    def hashMap(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
    
    # Sorting: Time O(n*lgn), Space O(1) or O(n)
    def sorting(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    
    # Bit Manipulation: Time O(n*logC), Space O(1)
    def bitManipulation(self, nums: List[int]) -> int:
        n = len(nums)
        majority_element = 0
        
        bit = 1
        for i in range(31):
            # Count how many numbers have the current bit set.
            bit_count = sum(bool(num & bit) for num in nums)

            # If this bit is present in more than n / 2 elements
            # then it must be set in the majority element.
            if bit_count > n // 2:
                majority_element += bit
            
            # Shift bit to the left one space. i.e. '00100' << 1 = '01000'
            bit = bit << 1
                
        # In python 1 << 31 will automatically be considered as positive value
        # so we will count how many numbers are negative to determine if
        # the majority element is negative.
        is_negative = sum(num < 0 for num in nums) > (n // 2)

        # When evaluating a 32-bit signed integer, the values of the 1st through 
        # 31st bits are added to the total while the value of the 32nd bit is 
        # subtracted from the total. This is because the 32nd bit is responsible 
        # for signifying if the number is positive or negative.
        if is_negative:
            majority_element -= bit
        
        return majority_element
    
    # Randomization: Time O(∞), Space O(1)
    def randomization(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
    
    # Divide and Conquer: Time O(n*lgn), Space O(lgn)
    def divideConquer(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)
    
    # Boyer-Moore Voting Algorithm: Time O(n), Space O(1)
    def boyerMoore(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
