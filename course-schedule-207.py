"""
Check if there is any cycle in the directed graph. More information:
- https://en.wikipedia.org/wiki/Topological_sorting#Algorithms
- https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/03Graphs.pdf

In this solution, I use the DFS method.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        for [a, b] in prerequisites:
            graph[a].append(b)

        def hasCycle(graph, maxCourse, n, visited):
            if n < maxCourse:
                return False

            if n in visited:
                return True

            visited.add(n)
            for m in graph[n]:
                if hasCycle(graph, maxCourse, m, visited):
                    return True

            visited.remove(n)
            return False

        for i in range(numCourses):
            if hasCycle(graph, i, i, set()):
                return False

        return True
