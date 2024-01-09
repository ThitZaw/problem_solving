#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        while root:
            # if p and q are lower than root, find in left side of the root
            if p.val < root.val and q.val < root.val:
                 root = root.left
                
            # if p and q are greater than root, find in right side of the root
            elif p.val > root.val and  q.val>root.val:
                root = root.right

            # if root == p or root == q or p < root < q or not root or dind what you need
            else:
                return root
        
# @lc code=end

