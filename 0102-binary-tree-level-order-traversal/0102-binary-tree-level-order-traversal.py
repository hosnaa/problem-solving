
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         sum_dict = {} # try to get the depth and embed this info
#         if root:
#             node_list = [root]
#             node_list_val = [[root.val]]
#             for node in node_list:
#                 if node:
#                     if node.left and node.right:
#                         node_list.append(node.left) 
#                         node_list.append(node.right)
#                         node_list_val.append([node.left.val, node.right.val])
#                     elif node.left and node.right is None:
#                         node_list.append(node.left) 
#                         node_list_val.append([node.left.val])
#                     elif node.left is None and node.right:
#                         node_list.append(node.right) 
#                         node_list_val.append([node.right.val])
#             return node_list_val  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return 
        else:
            node_list = [root]
            node_list_val = []
        while node_list:
            next_nodes = []
            current_nodes = []
            for node in node_list:
                current_nodes.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            node_list_val.append(current_nodes)
            node_list = next_nodes
        return node_list_val
            
            
        
        