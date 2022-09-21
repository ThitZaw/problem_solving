class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        res = []
        even_sum = sum([num for num in nums if num%2 == 0])
        for val,index in queries:
            if nums[index]%2 == 0: even_sum -= nums[index]
            nums[index] += val
            if nums[index]%2 == 0: even_sum += nums[index]
            res.append(even_sum)
        return res

sol = Solution()
res = sol.sumEvenAfterQueries(nums=[1],queries=[[4,0]])
print(res)