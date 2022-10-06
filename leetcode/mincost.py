class Solution:
    def minCost(self, colors, neededTime):
        output = prev = 0
        for curr in range(1,len(colors)):
            if colors[prev] == colors[curr]:
                output += min(neededTime[prev],neededTime[curr])
                if neededTime[prev] < neededTime[curr]:
                    prev = curr
            else:
                prev = curr
        return output

sol = Solution()
res = sol.minCost(colors="aaabbbabbbb"
,neededTime=[3,5,10,7,5,3,5,5,4,8,1])
print(res)