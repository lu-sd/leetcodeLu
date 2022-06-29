# 给你一个数组 nums 和一个值 val，你需要原地移除所有数值等于val的元素
# 并返回移除后数组的新长度。
class Solution:
      def removeElement(self,nums,val):
        fast = slow = 0
        while fast < len(nums):
        
            if nums[fast] != val:
               nums[slow] =nums[fast]
               slow += 1
            fast += 1
        return slow
       
A = Solution()
result = A.removeElement([0,1,2,2,4],2)
print(result)
