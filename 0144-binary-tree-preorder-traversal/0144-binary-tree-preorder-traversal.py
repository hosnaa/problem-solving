# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorderTraversal(self, root):
        mylist = []
        self.preorderTraversalHelper(root, mylist)
        return mylist
        
    
    def preorderTraversalHelper(self, root, mylist):
        if not root:
            return
        mylist.append(root.val)
        self.preorderTraversalHelper(root.left, mylist)
        self.preorderTraversalHelper(root.right, mylist)
    
        