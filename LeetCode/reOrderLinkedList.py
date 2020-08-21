# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if(head == None):
            return
        lstcopy = []
        temp = head

        #make a list of elements
        while(temp.next!=None):
            lstcopy.append(temp.val)
            temp=temp.next
        lstcopy.append(temp.val)
        lstcopy.reverse()
        temp=head
        index = 0 
        
        #make a new list with merging all the elements
        while(temp.next!=None):
            newnode = ListNode()
            newnode.val= lstcopy[index]
            newnode.next = temp.next
            temp.next = newnode
            temp = temp.next.next
            index+=1
        
        #trim the list to required elements
        temp=head
        index = 0     
        while(temp.next!=None):
            index+=1
            if(index>=len(lstcopy)):
                temp.next=None
                break
            temp=temp.next
