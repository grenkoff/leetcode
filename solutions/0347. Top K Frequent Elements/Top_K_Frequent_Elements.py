# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    # Bucket Sort Solution
    # Time: O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

a = Solution()

print(a.topKFrequent([1,4,4,1,1,2,2,4,4,4,4,4,4,3], 2))
print(a.topKFrequent([1], 1))
