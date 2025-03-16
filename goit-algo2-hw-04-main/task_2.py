from trie import Trie, TrieNode


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings or not all(isinstance(s, str) for s in strings):
            return ""

        self.root = TrieNode()
        for word in strings:
            self.put(word, True)

        prefix = ""
        node = self.root
        while len(node.children) == 1 and node.value is None:
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]

        return prefix


if __name__ == "__main__":
    lcp_trie = LongestCommonWord()
    test_strings = [
        ["flower", "flow", "flight"],
        ["interspecies", "interstellar", "interstate"],
        ["dog", "racecar", "car"],
        []
    ]
    for strings in test_strings:
        result = lcp_trie.find_longest_common_word(strings)
        print(f"Longest common prefix of {strings}: '{result}'")
