from cgitb import reset
from multiprocessing.reduction import duplicate


class Solution:
    def findErrorNums(self, nums):
        unique_nums = sum(set(nums))
        nums_len = len(nums)
        
        duplicate = sum(nums) - unique_nums
        miss = nums_len*(nums_len+1)//2 - unique_nums
        return [duplicate,miss]
       
            
                
sol = Solution()
res = sol.findErrorNums(nums=[3,2,2])
print(res)