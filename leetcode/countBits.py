class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n+1):
            ans.append("{0:b}".format(i).count("1"))
        return ans
                
sol = Solution()
print(sol.countBits(n=2))