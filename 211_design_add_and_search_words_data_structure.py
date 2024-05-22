class TrieNode:
    def __init__(self):
        # Initialize a Trie node with an empty dictionary for children
        # and a boolean flag indicating whether it's the end of a word
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:
    def __init__(self):
        # Initialize the WordDictionary with a root TrieNode
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root
        # Traverse each character in the word
        for char in word:
            # Use setdefault to get the child node or create a new one if it doesn't exist
            current_node = current_node.children.setdefault(char, TrieNode())
        # Mark the end of a word
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, index: int) -> bool:
            # If we've reached the end of the word, check if it's a valid word
            if index == len(word):
                return node.is_end_of_word

            if word[index] == ".":
                # If the current character is '.', try all possible children
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
            else:
                # If the character is in the children, continue the search with the child node
                if word[index] in node.children:
                    return dfs(node.children[word[index]], index + 1)

            # If no path matches, return False
            return False

        # Start DFS from the root node
        return dfs(self.root, 0)
