"""
4. Median of Two Sorted Arrays

nums1 = [1,3]
nums2 = [2]
output: 2

nums1 = [1,2]
nums2 = [3,4]
output: 2.5

:type nums1: List[int]
:type nums2: List[int]
:rtype: float
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        combo_list = []
        combo_list = nums1+nums2
        median = 0
        combo_list.sort()
        even_breaker = []

        if (len(combo_list) % 2) == 0:           #if even length
            for i, n in enumerate(combo_list):
                if i == (int(len(combo_list)/2)) or i == (int(len(combo_list)/2)-1):
                    even_breaker.append(n)
            median = sum(even_breaker)*.5


        elif (len(combo_list) % 2) != 0:                        #if odd length
            for i, n in enumerate(combo_list):
                if i == (int(len(combo_list)/2)):
                    median = n
                    
        return median
        