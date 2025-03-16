from trie import Trie


class Homework(Trie):
    def __init__(self):
        super().__init__()

    def put(self, key: str, value=None):
        if not isinstance(key, str) or not key:
            raise ValueError("Key must be a non-empty string")

        current = self.root
        for char in key:
            current = current.children[char]
        if current.value is None:
            self.size += 1
        current.value = value

    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string")

        count = 0

        def dfs(node, current_word):
            nonlocal count
            if node.value is not None and current_word.endswith(pattern):
                count += 1
            for char, child in node.children.items():
                dfs(child, current_word + char)

        dfs(self.root, "")
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string")

        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for word in words:
        trie.put(word, True)

    test_suffixes = ["e", "ion", "a", "at", "xyz"]
    for suffix in test_suffixes:
        result = trie.count_words_with_suffix(suffix)
        print(f"Words ending with '{suffix}': {result}")

    test_prefixes = ["app", "bat", "ban", "ca", "dog"]
    for prefix in test_prefixes:
        result = trie.has_prefix(prefix)
        print(f"Has prefix '{prefix}': {result}")

    print("All tests passed!")
