# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        newlist = []
        result = []
        if root == None:
            return newlist
        
        newlist.append(root)
        
        while(newlist):
            childlist = []
            for k in newlist:
                if k.left:
                    childlist.append(k.left)
                if k.right:
                    childlist.append(k.right)
            
            result.append(self.my_val(newlist))
            newlist = childlist
            
        return result[::-1]
    
    def my_val(self,l):
        result = []
        for item in l:
            result.append(item.val)
        return result
                
            
            