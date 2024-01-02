#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, string: str) -> bool:
        parentheses = {
            '{':'}','(':')','[':']'
        }
        output = []
        for s in string:
            if s in parentheses:
                output.append(parentheses[s])
            elif not output or output.pop() != s:
                return False
        return not output
# @lc code=end

