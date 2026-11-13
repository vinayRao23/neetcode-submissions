# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        stack = [(root, root.val)]
        count = 0
        
        while stack:
            node, max_val = stack.pop()
            
            if node.val >= max_val:
                count += 1
                
            current_max = max(max_val, node.val)
            
            if node.left:
                stack.append((node.left, current_max))
            if node.right:
                stack.append((node.right, current_max))
                
        return count