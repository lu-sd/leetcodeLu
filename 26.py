# 给你一个 升序排列 的数组 nums ，请你原地删除重复出现的元素
# 使每个元素 只出现一次 ，返回删除后数组的新长度。元素的相对顺序应该保持一致
from re import A


class Solution:
    def removeDuplicates(self, nums):
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


A = Solution()
result = A.removeDuplicates([2, 2, 3, 3, 5, 6])
print(result)
