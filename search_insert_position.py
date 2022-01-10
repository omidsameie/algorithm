'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''
import random
class Search_insert_position:
    def search(self, nums , target):
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                print('target found')
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        print('target should be inserted at:',right+1)
        return right+1
nums = sorted(random.sample(range(-1000,1000),1000))
target = random.sample(range(-1000,1000),1)[0]
p  = Search_insert_position()
res = p.search(nums, target)
