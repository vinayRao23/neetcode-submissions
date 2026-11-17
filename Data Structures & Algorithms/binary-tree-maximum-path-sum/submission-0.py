# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-infinity")

        def dfs(node):
            if not node:
                return 0
            
            left_side = max(0, dfs(node.left))
            right_side = max(0, dfs(node.right))

            curr = node.val + left_side + right_side

            self.max_sum = max(self.max_sum, curr)

            return node.val + max(left_side, right_side)
        
        dfs(root)
        return int(self.max_sum)
