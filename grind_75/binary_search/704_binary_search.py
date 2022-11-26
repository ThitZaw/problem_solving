class Solution:
    def search(self, nums, target):
        left, right = 0 , len(nums)-1
        while left <= right:
            mid = (left+right)//2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess < target:
                left = mid + 1
            else:
                right = mid -1

        return -1
    
sol = Solution()
res = sol.search(nums=[5],target=5)
print(res)
    
