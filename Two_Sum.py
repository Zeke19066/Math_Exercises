"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            print(f'n: {n}   i: {i}   h: {h}')

            if n not in h:
                h[num] = i
            else:
                print(f"Output: ({h[n]}, {i})")
                return [h[n], i]

Solution.twoSum(nums, target)