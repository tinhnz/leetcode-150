"""
Build a graph based on equations and values. Use a hash map to store the values of
a -> b and b -> a everytime we got a new equation. Use DFS to look for a path from
`start` to `end`. Return result if found a path, otherwise return -1.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


type Key = tuple[str, str]
type NodeMap = dict[Key, Node]
type ValueMap = dict[Key, float]


class Solution:
    def build(
        self, equations: list[list[str]], values: list[float]
    ) -> tuple[NodeMap, ValueMap]:
        valueMap = {}
        nodeMap = {}
        for i, e in enumerate(equations):
            valueMap[(e[0], e[1])] = values[i]
            valueMap[(e[1], e[0])] = 1 / values[i]

            if e[0] not in nodeMap:
                nodeMap[e[0]] = Node(e[0])

            if e[1] not in nodeMap:
                nodeMap[e[1]] = Node(e[1])

            nodeMap[e[0]].neighbors.append(nodeMap[e[1]])
            nodeMap[e[1]].neighbors.append(nodeMap[e[0]])

        return nodeMap, valueMap

    def calc(
        self,
        start: str,
        end: str,
        nodes: NodeMap,
        values: ValueMap,
    ) -> float:
        if start not in nodes or end not in nodes:
            return -1.0

        if start == end:
            return 1.0

        visited = set()
        stack = [(start, 1.0)]
        while len(stack):
            cur, res = stack.pop()
            if cur in visited:
                continue

            visited.add(cur)
            for neighbor in nodes[cur].neighbors:
                nxt = neighbor.val
                if nxt == end:
                    return res * values[(cur, nxt)]

                if nxt in visited:
                    continue

                stack.append((nxt, res * values[(cur, nxt)]))

        return -1.0

    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        result = []
        nodeMap, valueMap = self.build(equations, values)
        for q in queries:
            result.append(self.calc(q[0], q[1], nodeMap, valueMap))

        return result
