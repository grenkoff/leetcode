class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Stack-based solution Time: O(nlogn), Space: O(n)
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


a = Solution()

assert a.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
assert a.carFleet(10, [3], [3]) == 1
assert a.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
