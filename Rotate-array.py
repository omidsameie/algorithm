'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums) # k might be larger than the  length of the array
        l , r = 0, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        l , r = 0, k-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        l , r = k, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
