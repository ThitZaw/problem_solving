from calendar import c
import collections
from operator import index


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_list = collections.Counter(list(s)).most_common()
        str_char = ""
        for char,time in char_list:
            str_char += char * time
        return str_char
        

sol = Solution()
print(sol.firstUniqChar("leetcode"))