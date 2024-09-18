class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes, keys are characters
        self.children = {}
        # root {'a': <__main__.TrieNode object at 0x7ca6094bb010>, 'b': <__main__.TrieNode object at 0x7ca6094c8450>}
        # Boolean flag to mark if this node represents the end of a word
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        # Initialize the root node (an empty node)
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        current_node = self.root
        for char in word:
            # If the character is not already a child of the current node, add it
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            # Move to the next node (character)
            current_node = current_node.children[char]
        # After inserting all characters, mark the end of the word
        current_node.is_end_of_word = True

    def search(self, word):
        """
        Searches for an exact word in the trie.
        Returns True if the word exists, otherwise False.
        """
        current_node = self.root
        print("root", current_node)
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # Check if we are at the end of a valid word
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        """
        Checks if there is any word in the trie that starts with the given prefix.
        Returns True if a prefix exists, otherwise False.
        """
        current_node = self.root
       
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        # If we can traverse through all characters of the prefix, return True
        return True

    def delete(self, word):
        """
        Deletes a word from the trie if it exists.
        """

        # Recursive helper function to delete the word
        def delete_helper(node, word, depth):
            if not node:
                return False
            
            # If we've reached the end of the word
            if depth == len(word):
                # Word exists only if is_end_of_word is True
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    # If the node has no other children, it can be deleted
                    return len(node.children) == 0
                return False
            
            # Recur for the child node corresponding to the next character
            char = word[depth]
            if char in node.children:
                should_delete_child = delete_helper(node.children[char], word, depth + 1)
                
                # If the child should be deleted (no other children), remove it
                if should_delete_child:
                    del node.children[char]
                    # Return True if no children remain and this node isn't the end of another word
                    return len(node.children) == 0 and not node.is_end_of_word
            return False

        delete_helper(self.root, word, 0)



trie = Trie()
trie.insert("apple")

trie.insert("apricot")
trie.insert("bat")
trie.insert("bad")
print(trie)

print(trie.search("apple"))   # True
print(trie.search("bat"))     # True
print(trie.search("bats"))    # False
print(trie.starts_with("app"))  # True
print(trie.starts_with("ban"))  # False

# Delete a word
trie.delete("bat")
print(trie.search("bat"))     # False
print(trie.search("bad"))     # True  (bad still exists)
