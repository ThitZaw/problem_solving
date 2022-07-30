# Definition for singly-linked list.
from ast import dump


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 or not list2:
            return list1 or list2
        """
        dump and curr are refer to the same listNode object
        wheras curr move it's head to sort the obj but dump stay at 0 head
        """
        dump = curr = ListNode(0)
        while list1 != None and list2 != None:
            # check the smaller value and added to the curr 's curr.next 
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        # add what ever left of the list to 
        curr.next = list1 or list2
        # return dummp next because the curr started added at the second head and dump'next will give 
        # the second necessary 
        return dump.next
           
            
    
list1 = ListNode([1,2,4]) 
list2 = ListNode([1,3,4])
sol = Solution()
print(sol.mergeTwoLists(list1,list2))