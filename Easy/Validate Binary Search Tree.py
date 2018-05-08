# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        return self.check(root,float('-inf'),float('+inf'))
    def check(self,root,mini,maxi):
        if not root:
            return True
        if root.val <= mini:
            return False
        if root.val >= maxi:
            return False
        return self.check(root.left,mini,root.val) and self.check(root.right,root.val,maxi)
