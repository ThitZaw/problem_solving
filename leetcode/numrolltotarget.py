class Solution:
    """
        Ways(d,t) = Ways(d-1,t-1)+Ways(d-1,t-2)+...+Ways(d-1,t-k)
    """     
    def recur(self, n, k, target, lookup):
        # If target is not reachable then return 0
        if target <= 0 or target > n*k:
            return 0
        # If we are left with one dice and target is equal to any of the faces of dice then we have found a way so return 1
        if n == 1 and target <= k:
            return 1
        if (n, target) not in lookup:
            ways = 0
            for val in range(1, k+1):
                # Use the current dice, update the target as target - current face of dice and recur for remaining target with remaining dices
                ways += (self.recur(n-1, k, target-val, lookup))
            lookup[(n, target)] = ways
        return lookup[(n, target)] 
    
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self.recur(n, k, target, {}) % ((10**9) + 7)
    
    # def numRollsToTarget(self, n: int, k: int, target: int) -> int:        
    #     def helper(d,target):
    #         if target <= 0 or target > n*k:
    #             return 0
            
    #         if d == 1:
    #             return 1 if target <= k else 0
            
    #         if (n,target) not in dp:    
    #             res = 0
    #             for i in range(1,k+1):
    #                 res += helper(d-1,target-i)
    #             dp[(n, target)] = res
    #         return dp[(n, target)]
        
    #     dp = {}
    #     res = helper(n,target)
    #     return res % (10**9 + 7)
    
sol = Solution()
res = sol.numRollsToTarget(n=30,k=30,target=500)
print(res)