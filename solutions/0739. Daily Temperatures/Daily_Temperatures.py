class Solution:
    # def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Brute Force Time: O(n**2)
        # for 
        #     for


    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Monotonic Decreasing Stack Time: O(n)
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_ind = stack.pop()
                res[stack_ind] = i - stack_ind
            stack.append((t, i))
        return res


a = Solution()

assert a.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert a.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
assert a.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
