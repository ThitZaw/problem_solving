class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        output = False
        for row in matrix:
            if row[0] < target:
                output = target in row
        return output
    
sol = Solution()
assert sol.searchMatrix(matrix = [[1]], target = 1) == True