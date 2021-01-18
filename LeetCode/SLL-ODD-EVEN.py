# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        No_Nodes = 0
        if head == None:
            return head
        if head.next == None:
            return head
        headcopy = head.next
        oddhead = head
        evenhead = head.next
        evenlist = []
        while evenhead != None:
            evenlist.append(evenhead.val)
            if evenhead != None and evenhead.next!=None:
                evenhead = evenhead.next.next
            else:
                break
           
        evenlist.reverse()
        while headcopy != None:
            if oddhead!= None and oddhead.next != None:
                oddhead = oddhead.next.next
                if oddhead != None:
                    headcopy.val = oddhead.val
                    headcopy=headcopy.next
                else:
                    headcopy.val = evenlist.pop()
                    headcopy=headcopy.next
            else:
                headcopy.val = evenlist.pop()
                headcopy=headcopy.next
        return head
            