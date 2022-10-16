import math
class Solution:
    def increasingTriplet(self, nums):
        first = second = math.inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:  # Now first < num, if num <= second then try to make `second` as small as possible
                second = num
            else:  # Now first < second < num
                return True
        return False
            
            
    
sol = Solution()
res = sol.increasingTriplet([2,1,5,0,4,6])
print(res)