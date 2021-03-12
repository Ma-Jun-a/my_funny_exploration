import time模块
def timer(func, *args):
    start = time模块.clock()
    func(*args)
    return time模块.clock() - start
# print(timer)
def sum_two(nums, target):
    nums.sort()
    for index, i in enumerate(nums):
        if target > (i * 2):
            nums1 = nums[index:]
            for x in nums1:
                if i + x == target:
                    return index, nums.index(x)
                else:
                    continue
        else:
            continue

nums = list(range(100000))
# nums = li.extend([2, 7, 11, 15,])
target = 9
s = sum_two(nums, target)
print(s)
print(timer(sum_two,nums,target))

def sum_one(nums, target):
    for i in nums:
        for x in nums:
            if i + x == target:
                return nums.index(i),nums.index(x)
            else:continue
        else:continue
print(sum_one(nums,target))
print(timer(sum_one,nums,target))

