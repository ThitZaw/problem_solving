class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        output = False
        s_index = t_index = 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
                
        return s_index == len(s)

sol = Solution()
print(sol.isSubsequence(s = "acb", t = "ahbgdc"))