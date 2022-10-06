from operator import eq
import string


class Solution:
    def equationsPossible(self, equations):
        parent = {}
        def find(x):
            parent[x] = parent.get(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x]) ##path compression
            return parent[x]
                
        for a,sign,_,b in equations:
            if sign == "=":
                x = find(a)
                y = find(b)
                parent[x]= y
        
        for a,sign,_,b in equations:
            if sign == "!":
                if find(a) == find(b):
                    return False
        return True

    
sol = Solution()
res = sol.equationsPossible(equations = ["b==a","a==b"])
print(res)