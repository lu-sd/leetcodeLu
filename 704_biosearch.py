class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle

        return -1


alist = [1, 3, 6, 8, 9]
targrt = 8
A = Solution()
result = A.search(alist, target=8)
print(result)
