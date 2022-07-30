class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = []
        for no in range(len(nums)):
            complement = target-nums[no]
            occ = [index for index,value in enumerate(nums) if value == complement and index != no]
            if occ:
                return (no,occ[0])

sol = Solution()
sol.twoSum([2,7,11,15],9)