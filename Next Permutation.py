'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.


Given a word, find the lexicographically greater permutation of it. For example, lexicographically next permutation of “gfg” is “ggf” and 
next permutation of “acb” is “bac”.Note: In some cases, the next lexicographically greater word might not exist, e.g, “aaa” and “edcba”

    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.

Input
[3,2,1]
Output
[3,2,1]
Expected
[1,2,3]

'''
nums = [3,2,1]
Answer = [1,2,3]

'''
nums = [1,2,3]
Answer = [1,3,2]
'''

class Solution(object):
    def nextPermutation(self, nums):
        output = []
        failed = False
        marker = 0


        for i, n in enumerate(nums):
            if i > 0: #We wanna skip the first one since there's nothing to compare it to. 
                if (n > nums[i-1]) and (n > marker):
                    marker = i -1

                    print(f'New Greatest: {n}')

        if marker != 0:
            popped = nums.pop()
            print(f'Popped: {popped}')
            nums.insert(marker, popped)
            return(nums)

        if marker == 0:
            output = []
            while len(nums) > 0:
                for i, n in enumerate(nums):
                    if n <= nums[marker]:
                        marker = i
                output.append(nums[marker])
                del nums[marker]
                marker = 0
            return output


launcher = Solution()
print(launcher.nextPermutation(nums))