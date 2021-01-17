"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

:type nums: List[int]
:rtype: List[int]
"""

class Solution(object):
    def runningSum(self, nums):
        l = []
        lv = 0     #storing the last value
        for i, n in enumerate(nums):
            if i == 0:
                l.append(n)
                lv = n
            elif i != 0:
                l.append(n+lv)
                lv = n+lv
        
        return l
            
"""
Success:

Runtime: 16 ms, faster than 99.77% of Python online submissions for Running Sum of 1d Array.
Memory Usage: 13.3 MB, less than 50.58% of Python online submissions for Running Sum of 1d Array.
"""