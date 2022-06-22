class Solution:
    def twosum(self, nums, target):
        mapping = {}
        for index, value in enumerate(nums):
            diff = target-value
            if diff not in mapping:
                mapping[value] = index
            else:
                return [index, mapping[diff]]

input = [2,7,11,15] 

target = 9
A = Solution()
result = A.twosum( input, 9 )
print(result)

