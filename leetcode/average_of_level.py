# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
            add node to queue
            add sum
        
        """        
        queue,avg = collections.deque([root]),[] # add the first node in the queue
        while queue:
            node_sum = 0 # sum of each level
            node_len = len(queue) # each level total num
            for i in range(node_len): # loop each 
                node = queue.popleft() 
                node_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg.append(node_sum/node_len) # avg = sum/len
        return avg