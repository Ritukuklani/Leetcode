# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        stack = [(root, root.val, root.val)]
        ans = float("-inf")
        while stack:
            node, min_val, max_val = stack.pop()
            if node.left:
                stack.append((node.left, min(min_val, node.left.val), max(max_val, node.left.val)))
            if node.right:
                stack.append((node.right, min(min_val, node.right.val), max(max_val, node.right.val)))
            ans = max(ans, abs(node.val - min_val), abs(node.val - max_val))
        return ans