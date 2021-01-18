# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        count = 1
        headcopy = head
        if head==None:
            return True 
        if head.next ==None:
            return True
        while headcopy.next!=None:
            count+=1
            headcopy = headcopy.next
        count=count/2
        while head!=None:
            if count>0.5:
                vals.append(head.val)
            elif count==0.5:
                pass
            elif(head.val==vals[-1]):
                vals.pop()
            else:
                return False
            count-=1

            head = head.next
        
        return True