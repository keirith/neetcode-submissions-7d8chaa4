# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
            
        stack = [ (root, root.val) ]

        while stack:
            curr, path_sum = stack.pop()

            if curr.left is None and curr.right is None:
                if path_sum == targetSum:
                    return True

            if curr.right:
                stack.append((curr.right, path_sum + curr.right.val))
            if curr.left:
                stack.append((curr.left, path_sum + curr.left.val))
        
        return False