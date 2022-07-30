from calendar import c
import collections
from operator import index


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_list = collections.defaultdict(lambda: s.count(c))
        unique_word = []
        for i,c in enumerate(s):
            if char_list[c] < 2 :
                unique_word.append(i)
        return unique_word[0] if unique_word else -1
        

sol = Solution()
print(sol.firstUniqChar("leetcode"))