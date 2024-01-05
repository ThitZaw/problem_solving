#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = set()
        # count the odd number in the string
        for letter in s:
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)
        # there is no odd number character in string
        if len(ss) == 0: 
            return len(s)
        # return even count char (s - ss) + 1 (we gonna use only one character among odd count)
        else: 
            return len(s) - len(ss)+1
        
# @lc code=end

