from collections import Counter
from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def counter(start, last, last_count, left):
            if left < 0:
                return float('inf')
            if start >= len(s):
                return 0
            if s[start] == last:
                incr = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0
                return incr + counter(start+1, last, last_count+1, left) 
            else:
                keep_counter = 1 + counter(start+1, s[start], 1, left)
                del_counter =  counter(start + 1, last, last_count, left - 1)
                return min(keep_counter, del_counter)
            
        return counter(0, "", 0, k)     
    
sol = Solution()
res = sol.getLengthOfOptimalCompression(s="aaabcccd",k=2)
# assert res == 4
# res2 = sol.getLengthOfOptimalCompression(s="aabbaa",k=2)
# assert res2 == 2
# res3 = sol.getLengthOfOptimalCompression(s="aaaaaaaaaaa",k=0)
# assert res3 == 2
# res4 = sol.getLengthOfOptimalCompression(s="aabaabbcbbbaccc",k=6)