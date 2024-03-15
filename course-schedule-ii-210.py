"""
Find a topological sort of given graph. More information:
- https://en.wikipedia.org/wiki/Topological_sorting#Algorithms
- https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/03Graphs.pdf

In this solution, I use the DFS method.
"""


class Solution:
    def build(self, result, graph, marked, visited, cur):
        if cur in marked:
            return True

        if cur in visited:
            return False

        visited.add(cur)
        for nxt in graph[cur]:
            if not self.build(result, graph, marked, visited, nxt):
                return False

        visited.remove(cur)
        result.append(cur)
        marked.add(cur)
        return True

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for i in range(numCourses)]
        for [a, b] in prerequisites:
            graph[a].append(b)

        result = []
        marked = set()
        for c in range(numCourses):
            if not self.build(result, graph, marked, set(), c):
                return []

        return result
