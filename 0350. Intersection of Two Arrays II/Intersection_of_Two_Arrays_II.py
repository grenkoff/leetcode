class Solution:
    # HashMap Approach
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        res = []
        for i in nums2:
            if c[i] > 0:
                res.append(i)
                c[i] -= 1
        return res
    
    # Two Pointers Approach
    def twoPointers(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j = 0, 0
        res = []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
