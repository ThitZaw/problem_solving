class Solution:
    """we can solved this problem :
        given : the left of the index is equal to the sum of all the numbers strictly to the index's right.
                left_sum == right_sum
                
              :If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
              This also applies to the right edge of the array. then - left = 0
              
        nums = [1,7,3,6,5,6]      left_sum = 0   right_sum = sum(nums) = 28
        1st num = 1
        -------------
        [1,7,3,6,5,6]      left_sum = 0+ num = 0 + 1 = 1  left != right    right_sum = 28 - num = 28 - 1 = 27
        
        2nd mum = 7
        -------------
        [7,3,6,5,6]      left_sum = 1 + num = 1 + 7 = 8   left != right   right_sum = 27 - num = 27 - 7 = 20
        
        3rd  num = 3
        -------------
        [3,6,5,6]      left_sum = 8 + num = 8 + 3 = 11   left != right   right_sum = 20 - num = 20 - 3 = 17

        4th  num = 6
        -------------
        [6,5,6]      left_sum = 11 + num = 11 + 6 = 17   left == right  return True

    """
    def pivotIndex(self, nums):
        left = 0
        right = sum(nums)
        for index,num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1
    
sol = Solution()
sol.pivotIndex([1,7,3,6,5,6])