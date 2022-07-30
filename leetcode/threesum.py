class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        i -> loop through nums
        ^
        |
        [][][][][].sorted()
          |      |
          V      V
          j      k        
        """
        nums.sort()
        result = []
        for i in range(len(nums) - 2): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            j,k = i + 1,len(nums) -1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum < 0:j += 1 
                elif curr_sum > 0:k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:j += 1
                    while j < k and nums[k] == nums[k - 1]:k -= 1
                    j += 1
                    k -= 1
        return result
Sol = Solution()
print(Sol.threeSum(nums = [-1,0,1,2,-1,-4]))