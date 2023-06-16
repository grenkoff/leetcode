class Solution:
    # Brute Force Solution
    # Time: O(n ** 2)
    #def twoSum(self, numbers: List[int], target: int) -> List[int]:


    # Two Pointers Solution
    # Time: O(n), Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            current = numbers[l] + numbers[r]
            if current > target:
                r -= 1
            elif current < target:
                l += 1
            else:
                return [l + 1, r + 1]
