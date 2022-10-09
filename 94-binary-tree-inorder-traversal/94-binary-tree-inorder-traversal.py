# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree_list = []
        # no need to return the tree as it's already being updated in the same place (reference)
        self.inorderTraversalHelper(root, tree_list)
        return tree_list
    def inorderTraversalHelper(self, node, tree_list):
        # stopping condition: first to write in recursion; 
        # if this node is none then we won't proceed
        if not node:
            return
        self.inorderTraversalHelper(node.left, tree_list)
        tree_list.append(node.val) # we only append the value of this node: while left and right are used for traversal not addition of values since during the traceback of the call stack you'll be adding these nodes
        self.inorderTraversalHelper(node.right, tree_list)
        