# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        present_root = root
        p_val = p.val
        q_val = q.val
        while present_root:
            present_val = present_root.val
            if p_val>present_val and q_val>present_val:
                present_root = present_root.right
            elif p_val<present_val and q_val<present_val:
                present_root = present_root.left
            else:
                return present_root
            