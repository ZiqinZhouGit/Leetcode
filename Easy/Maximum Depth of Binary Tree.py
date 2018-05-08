# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        leftDepth = self.maxDepth(root.left) if root.left else 1
        rightDepth = self.maxDepth(root.right) if root.right else 1   
        return max(leftDepth, rightDepth) + 1
