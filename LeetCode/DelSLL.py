# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None or head.next == None:
            return head
        realhead = head
        while(head != None and head.next != None):
            while head!= None and head.next != None and head.val==head.next.val:
                head.next = head.next.next
            
            
            head = head.next
            
        return realhead