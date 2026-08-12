# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #solve DFS recursively
        #base case - handling a null node
        if root is None:
            return None

        #recursive step
        #save original copy of left and right branches
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        #swap branches
        root.left = right
        root.right = left

        return root
        