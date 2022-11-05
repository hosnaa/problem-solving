"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ## Take nodes; make recursion until it's null 
        tree = []
        self.preorderHelper(root, tree)
        return tree
    
    def preorderHelper(self, root, tree):
        if not root:
            return
        tree.append(root.val)
        for child in root.children:
            self.preorderHelper(child, tree)
        