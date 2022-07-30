from itertools import count


class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        old_mat = [mat_c for mat_r in mat for mat_c in mat_r]
        new_mat = r*c
        remat = []
        if len(old_mat) != new_mat:
            return mat
        count = 0
        for new_r in range(r):
            temp = []
            for new_c in range(c):
                temp.append(old_mat[count])
                count += 1
            remat.append(temp)
        return remat
                
        
sol = Solution()
sol.matrixReshape(mat=[[1,2],[3,4]], r = 1, c = 4)