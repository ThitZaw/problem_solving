# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head: ListNode)  -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

sol = Solution()
print(sol.reverseList(head = [1,2,3,4,5]))