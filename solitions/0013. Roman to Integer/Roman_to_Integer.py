#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'CM': 900, 'CD':400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4, 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'III': 3, 'II': 2, 'I': 1}
        res = 0
        while s != '':
            for i in roman:
                if i in s:
                    res += roman[i]
                    s = s.replace(i, '', 1)
        return res
