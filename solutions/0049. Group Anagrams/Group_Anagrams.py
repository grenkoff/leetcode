# https://leetcode.com/problems/group-anagrams/

class Solution:
    '''HashMap Solution
    Time: O(m * n), m is the number of strings we`re given,
    n is the average length of each string'''
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return res.values()


a = Solution()

print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
print(a.groupAnagrams([""])) # dict_values([['']])
print(a.groupAnagrams(["a"])) # dict_values([['a']])