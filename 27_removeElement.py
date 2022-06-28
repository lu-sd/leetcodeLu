


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
