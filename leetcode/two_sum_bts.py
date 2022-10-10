# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def helper(node,nums,complement):
            if not node:
                return False
            complement = k- node.val
            if complement in nums:
                return True
            
            nums.append(node.val)
            
            return helper(node.left,nums,k) or helper(node.right,nums,k)
        
        if not root:
            return False
        return helper(root,[],k)