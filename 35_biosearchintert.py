from re import A


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
