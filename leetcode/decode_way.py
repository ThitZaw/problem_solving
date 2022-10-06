class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        
        for i in range(len(s)-1,-1,-1):
            s_1 = s[i]
            
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                s_2 = s[i+1]
                dp[i] += dp[i+2]
                
         
        return dp[0]
    
sol = Solution()

res = sol.numDecodings("2611055971756562")        
print(res)      