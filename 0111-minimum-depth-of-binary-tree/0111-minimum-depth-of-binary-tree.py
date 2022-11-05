# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
### The problem in normal iterative is that you'll be updating twice in the depth; using a flag also didn't work (why?)

import collections

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
        
#         node_list = [root]
#         depth = 1
#         while node_list:
#             next_nodes = []
#             flag_node = False
#             for node in node_list:
#                 if node:
#                     if not node.left and not node.right:
#                         return depth
#                     if node.left:
#                         next_nodes.append(node.left)
#                         flag_node = True # flag if we found a node then we shall increase the depth
#                     if node.right:
#                         next_nodes.append(node.right)
#                         flag_node = True
         
#                     if flag_node:
#                         depth += 1
#                     node_list = next_nodes
#                 else:
#                     return 0
        
        