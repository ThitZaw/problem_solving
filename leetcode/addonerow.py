# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,val,depth,level):
            if depth-1 == level: # add လုပ်ရမယ့် level 
                root.left = TreeNode(val=val,left=root.left)
                root.right = TreeNode(val=val,right=root.right)
                return
            if root.left:
                self.helper(root.left,val=val,depth=depth,level=level+1)
            if root.right:
                self.helper(root.right,val=val,depth=depth,level=level+1)

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val,left=root) #create new treeNode
        self.helper(root,val,depth,1)
        return root

