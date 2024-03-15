"""
Use a hash map to store new nodes. Traversal through the original graph using DFS,
and create new nodes when needed.
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        nodeMap = {1: Node(1)}
        stack = [node]
        visited = set()
        while len(stack):
            cur = stack.pop()
            if cur.val in visited:
                continue

            visited.add(cur.val)
            if cur.val not in nodeMap:
                nodeMap[cur.val] = Node(cur.val)

            for neighbor in cur.neighbors:
                if neighbor.val not in visited:
                    stack.append(neighbor)

                if neighbor.val not in nodeMap:
                    nodeMap[neighbor.val] = Node(neighbor.val)

                nodeMap[cur.val].neighbors.append(nodeMap[neighbor.val])

        return nodeMap[1]
