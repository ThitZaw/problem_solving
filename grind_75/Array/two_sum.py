class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index,value in enumerate(nums):
            complement = target - value
            if complement in nums and nums.index(complement) != index:
                return [index,nums.index(complement)]