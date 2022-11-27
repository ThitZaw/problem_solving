class Solution:
    def search(self, nums, target):
        ''''
            - check if mid indec 's left or right is asc sorted 
            - search target in the sorted side
        '''
        left,right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            # t = 0,m = 3 left rotate : [4,5,6,7,0,1,2] 
            if nums[left] > nums[mid]: # for left rotated
                if nums[mid] < target <= nums[right]:
                    left = mid +1
                else:
                    right = mid -1
            else:# for right rotated
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1                   
                
        return -1
    
sol = Solution()
res = sol.search(nums=[6,7,0,1,2,4,5],target=0)
print(res)