# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        visible = []
        queue = deque([root])

        while queue:
            last_node = None
            queueLen = len(queue)
            for i in range(queueLen):
                node = queue.popleft()
                if node:
                    last_node = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if last_node:
                visible.append(last_node.val)
        
        return visible
