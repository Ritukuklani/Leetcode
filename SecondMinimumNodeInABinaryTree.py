# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        stack = []
        stack.append(root)
        curr_next_min = float("inf")
        while stack:
            root = stack.pop()
            if root.left and root.right and root.val==root.left.val==root.right.val:
                stack.append(root.left)
                stack.append(root.right)
            elif root.left and root.val==root.left.val:
                if root.right and root.right.val<curr_next_min:
                    curr_next_min = root.right.val
                else:
                    break
                stack.append(root.left)
            elif root.right:
                if root.left and root.left.val<curr_next_min:
                    curr_next_min = root.left.val
                else:
                    break
                stack.append(root.right)
        return curr_next_min if curr_next_min!=float("inf") else -1