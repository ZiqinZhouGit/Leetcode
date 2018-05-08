# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        return self.BFS(root)
    def BFS(self,node):
        if not node:
            return []
        queue = [[node]]
        count = 0
        while count < len(queue):
            temp_level =[]
            for node in queue[count]:
                if node.left:
                    temp_level.append(node.left)
                if node.right:
                    temp_level.append(node.right)
            if temp_level != []:
                queue.append(temp_level)
            count += 1
        return [[x.val for x in level] for level in queue]
