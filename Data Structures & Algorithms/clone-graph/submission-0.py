"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        seen = set()
        dictionary = defaultdict()

        def dfs(curr):
            if not curr:
                return None
            if curr in seen:
                return dictionary[curr]
            seen.add(curr)

            cloned_node = Node(curr.val)
            dictionary[curr] = cloned_node

            for neighbor_node in curr.neighbors:
                cloned_neighbor = dfs(neighbor_node)
                
                if cloned_neighbor:
                    cloned_node.neighbors.append(cloned_neighbor)
            
            return dictionary[curr]

        return dfs(node)