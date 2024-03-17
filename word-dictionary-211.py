"""
Apply DFS when searching to address the problem of dot characters.
"""


class Node:
    def __init__(self, terminal: bool = False):
        self.terminal = terminal
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()

            node = node.children[char]

        node.terminal = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)

    def dfs(self, node: Node, word: str) -> bool:
        if word == "":
            return node.terminal

        char = word[0]
        if char == ".":
            if not len(node.children):
                return False

            for n in node.children.values():
                if self.dfs(n, word[1:]):
                    return True

        if char not in node.children:
            return False

        return self.dfs(node.children[char], word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
