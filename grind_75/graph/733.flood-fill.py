#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
            
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col , value = len(image),len(image[0]),image[sr][sc]
        
        def dfs(sr,sc):
            if 0 <= sr < row and 0 <= sc < col and image[sr][sc] == value:
                image[sr][sc] = color
                dfs(sr+1,sc+0)
                dfs(sr-1,sc+0)
                dfs(sr+0,sc+1)
                dfs(sr+0,sc-1)

        if value != color:
            dfs(sr,sc)
        return image
            
# @lc code=end

