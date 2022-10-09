# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree_list = []
        self.postorderTraversalHelper(root, tree_list)
        return tree_list
    
    def postorderTraversalHelper(self, node, tree_list):
        if not node:
            return
        self.postorderTraversalHelper(node.left, tree_list)
        self.postorderTraversalHelper(node.right, tree_list)
        tree_list.append(node.val)
        