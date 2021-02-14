# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        origheadA = headA
        origheadB = headB
        headaflag = True
        headbflag = True
        while(headA!=None and headB!=None):
            if headA==headB:
                return headA
            else:
                headA= headA.next
                headB= headB.next
            if headA == None and headaflag:
                headA = origheadB
                headaflag = False
            if headB == None and headbflag:
                headB = origheadA
                headbflag = False
                
        return None
