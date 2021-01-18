# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        headsList = []
        while(head!=None):
            if head.next in headsList:
                return True
            else:
                headsList.append(head.next)
                head = head.next
                
        return False