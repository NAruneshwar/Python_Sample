# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        comblist = ListNode()
        orignode = comblist
        while l1!=None or l2!=None:
            comblist.next = ListNode()
            comblist = comblist.next
            if(l1==None):
                comblist.val = l2.val
                l2=l2.next
                comblist.next = ListNode()
            elif(l2==None):
                comblist.val = l1.val
                l1=l1.next
                comblist.next = ListNode()
            elif(l1.val>l2.val):
                comblist.val = l2.val
                l2=l2.next
                comblist.next = ListNode()
            elif(l2.val>l1.val):
                comblist.val = l1.val
                l1 = l1.next
            elif(l1.val==l2.val):
                comblist.val = l1.val
                comblist.next = ListNode()
                comblist = comblist.next
                comblist.val = l2.val
                l1 = l1.next
                l2 = l2.next
        
        comblist.next = None
        return orignode.next