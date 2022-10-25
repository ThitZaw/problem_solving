from collections import Counter
class Solution:
    def maxlength(self, arr):
        charset = set()
        def duplicate(charset, s):
            c = Counter(charset) + Counter(s)
            return max(c.values()) > 1

        def backtrack_helper(i):
            if i == len(arr):
                return len(charset)
            res= 0
            if not duplicate(charset, arr[i]): 
                for c in arr[i]:# choose
                    charset.add(c)
                res = backtrack_helper(i+ 1) # explore
                for c in arr[i]: # unchoose
                    charset.remove(c)
            return max(res, backtrack_helper(i + 1)) # dont concatenate arr[i]
        return backtrack_helper(0)
    
sol = Solution()
res = sol.maxlength(["un","iq","ue"])
print(res)