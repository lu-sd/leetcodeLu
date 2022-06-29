# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

class Solution:
    def searchinsert(self, nums, target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return right + 1


A = Solution()
result = A.searchinsert([2,3,4,5,9], 4)
print(result)
