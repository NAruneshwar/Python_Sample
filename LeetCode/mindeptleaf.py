# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        level = 1
        nodes = []
        nodes.append(root)
        newnodes = []
        while(nodes):
            newnodes = []
            for k in nodes:
                if(k.left==None and k.right==None):
                    return level
                if(k.left!=None):
                    newnodes.append(k.left)
                if(k.right!=None):
                    newnodes.append(k.right)
            
            nodes = newnodes
            level+=1
