import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = dict(collections.Counter(list(s)).most_common())
        for char in list(t):
            if char in s_list:
                s_list[char] -= 1
            else:
                return False
        return any(value== 0 for value in s_list.values())        
        
sol = Solution()
print(sol.isAnagram(s = "ab", t = "a"))
                                     
        