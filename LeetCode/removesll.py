# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        he = ListNode()
        he.val = -1
        he.next = head
        if head==None:
            return head
        head = he
        while(head.next!=None):
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return he.next
        