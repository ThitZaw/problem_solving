# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,max_num):
            if not root:
                return 0
            
            good_node = 1 if root.val >= max_num else 0 # check if X is greater than max_num
            max_num = max(root.val,max_num)
                
            good_node += dfs(root.left,max_num) # go to left side of node
            good_node += dfs(root.right,max_num) # go to right side of node
            return good_node
        
        res = dfs(root,root.val)
        return res
