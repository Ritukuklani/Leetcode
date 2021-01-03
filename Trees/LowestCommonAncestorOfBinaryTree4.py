# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)

        def traverse(node): 
            if not node: return None
            if node in nodes: return node
            left =  traverse(node.left)
            right = traverse(node.right)
            if left and right: return node
            if left: return left
            return right
        return traverse(root)