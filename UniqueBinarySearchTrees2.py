# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int): #return type : List[TreeNode]:
        memo = {}
        def helper(s,e):
            if (s, e) in memo:
                return memo[(s, e)]
            if s>e:
                return [None,]
            all_trees = []
            for i in range(s, e+1):
                left = helper(s, i-1)
                right= helper(i+1,e)
                for l in left:
                    for r in right:
                        curr_tree = TreeNode(i)
                        curr_tree.left = l
                        curr_tree.right = r
                        all_trees.append(curr_tree)
            memo[(s, e)] = all_trees
            return all_trees
        return helper(1,n) if n else []