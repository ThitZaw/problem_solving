class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in range(0,len(nums)-1):
            j = i+1
            if j == len(nums):
                return False
            if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
                return True

            
sol = Solution()
print(sol.containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0))