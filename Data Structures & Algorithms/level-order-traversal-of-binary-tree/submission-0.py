# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level = 0
        queue = deque([ (root, level) ])
        result = []

        while queue:
            (current, level) = queue.popleft()
            if level == len(result):
                result.append([])
            result[level].append(current.val)

            if current.left:
                queue.append((current.left, level + 1))
            
            if current.right:
                queue.append((current.right, level + 1))

        return result