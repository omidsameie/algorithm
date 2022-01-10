import random
class Binary_search:
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
        print('target not found')
        return -1
nums = sorted(random.sample(range(-1000,1000),1000))
target = random.sample(range(-1000,1000),1)[0]
p  = Binary_search()
res = p.search(nums, target)
