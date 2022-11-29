# https://leetcode.com/problems/longest-common-prefix/

import sys
class Solution:
    # Horizontal scanning
    # Time: O(S), where S is the sum of all characters in all strings; Space: O(1)
    def horizontalScanning(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
    
    # Vertical scanning
    # Time: O(S), where S is the sum of all characters in all strings; Space: O(1)
    def verticalScanning(self, strs: List[str]) -> str:
        res = ''
        if len(strs) == 0:
            return res
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
    
    # Solution with sort() and zip()
    # Time: O(?), Space: O(?)
    def sortZip(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        res = ''
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                res += x
            else:
                break
        return res
    
    # Divide and Conquer
    # Time: O(?), Space: O(?)
    def divideConquer(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        return self.divide(strs, 0, len(strs) - 1)
    def divide(self, strs, left, right):
        if left == right:
            return strs[left]
        else:
            mid = (left + right) // 2
            lcpLeft = self.divide(strs, left, mid)
            lcpRight = self.divide(strs, mid+1, right)
            return self.conquer(lcpLeft, lcpRight)
    def conquer(self, left, right):
        m = min(len(left), len(right))
        for i in range(m):
            if left[i] != right[i]:
                return left[:i]
            i += 1
        return left[:m]
    
    # Binary Search
    # Time: O(?), Space: O(?)
    def binarySearch(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        minLen = sys.maxsize
        for str in strs:
            minLen = min(minLen, len(str))
        low = 1
        high = minLen
        while low <= high:
            mid = (low + high) // 2
            if self.isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][:(low + high) // 2]
    def isCommonPrefix(self, strs, len):
        str1 = strs[0][:len]
        i = 1
        while i < strs.__len__():
            if not strs[i].startswith(str1):
                return False
            i += 1
        return True
