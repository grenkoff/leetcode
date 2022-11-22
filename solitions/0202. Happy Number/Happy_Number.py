# https://leetcode.com/problems/happy-number/

# Approach 1: Detect Cycles with a HashSet
class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

# Approach 2: Floyd's Cycle-Finding Algorithm

# Approach 3: Hardcoding the Only Cycle (Advanced)

# Approach 3: Hardcoding 4
