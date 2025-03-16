from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def put(self, key: str, value=None):
        if not key:
            raise ValueError("Key must be a non-empty string")

        current = self.root
        for char in key:
            current = current.children[char]
        if current.value is None:
            self.size += 1
        current.value = value

    def get(self, key: str):
        if not key:
            raise ValueError("Key must be a non-empty string")

        current = self.root
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.value

    def delete(self, key: str):
        if not key:
            raise ValueError("Key must be a non-empty string")

        def _delete(node, key, depth):
            if depth == len(key):
                if node.value is not None:
                    node.value = None
                    self.size -= 1
                    return not node.children
                return False

            char = key[depth]
            if char in node.children and _delete(node.children[char], key, depth + 1):
                del node.children[char]
                return not node.children and node.value is None
            return False

        _delete(self.root, key, 0)
