# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorderTraversal(self, root):
        ## This only runs once and its benefit is just to initialize (outside the recursion) a list that you can append to without losing it. 
        tree = []
        self.preorderTraversalHelper(tree, root) # no need to return anything as we pass it by reference (both point to same thing thus it changes)
        # print('hello')
        return tree
        
    def preorderTraversalHelper(self, tree, node: Optional[TreeNode]) -> List[int]:
        if not node:
            return
        tree.append(node.val) 
        self.preorderTraversalHelper(tree, node.left) # at the end of this stack; the node itself will be the root's left child and so on all lefts; and inside each left there will be rights (since each left is a complete new call)
        self.preorderTraversalHelper(tree, node.right)        
        