# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # make level order then count
        if not root: 
            return 0
        node_list = [root]
        level = 1
        flag = False
        while node_list:
            next_nodes = []
            for node in node_list: # node_list already gets updated each time by the children
                if node.left:
                    next_nodes.append(node.left)
                    flag = True
                if node.right:
                    next_nodes.append(node.right)
                    flag = True
            node_list = next_nodes
            if flag: ## flag to avoid incrementing the level while the children are none
                level += 1
            flag = False
        return level

        