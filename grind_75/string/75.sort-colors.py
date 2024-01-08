#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        0 = red,  1 = white , 2 = blue
        """
        left , curr , right = 0 , 0 , len(nums) -1
        while curr <= right:
            # if current is 0 swap with left
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
            # if current is 2 swap with right
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
                curr -= 1
            curr += 1
        
# @lc code=end

