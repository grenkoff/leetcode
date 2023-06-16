class Solution:
    # Brute Force Solution
    # Time: O(n ** 2)
    #def twoSum(self, numbers: List[int], target: int) -> List[int]:


    # Two Pointers Solution
    # Time: O(n), Space: O(1)
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            current = numbers[l] + numbers[r]
            if current > target:
                r -= 1
            elif current < target:
                l += 1
            else:
                return [l + 1, r + 1]

a = Solution()

print(a.twoSum([1, 3, 4, 5, 7, 10, 11], 9)) # [3, 4]
print(a.twoSum([2, 7, 11, 15], 9)) # [1, 2]
print(a.twoSum([2, 3, 4], 6)) # [1, 3]
print(a.twoSum([-1, 0], -1)) # [1, 2]
