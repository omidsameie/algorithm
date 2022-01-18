'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j=0,0
        while j < len(nums):
            if nums[j]==0:
                j+=1
            else:
                nums[i]=nums[j]
                i +=1
                j +=1
        while i <len(nums):
            nums[i]=0
            i +=1
