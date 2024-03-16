"""
This is an easy BFS traversal problem.
"""

from collections import deque


class Solution:
    def canMutate(self, a: str, b: str) -> bool:
        count = 0
        for i in range(8):
            if a[i] != b[i]:
                count += 1
        return count <= 1

    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        marked = {startGene}
        mutaQ = deque()
        stepQ = deque()
        mutaQ.append(startGene)
        stepQ.append(0)
        while len(mutaQ):
            curGene = mutaQ.popleft()
            curStep = stepQ.popleft()
            if curGene == endGene:
                return curStep

            for nxtGene in bank:
                if nxtGene in marked:
                    continue

                if self.canMutate(curGene, nxtGene):
                    marked.add(nxtGene)
                    mutaQ.append(nxtGene)
                    stepQ.append(curStep + 1)

        return -1
