"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""


class TrieNode:
    # Initialize your data structure here.
    def __init__(self, isWord = False):
        self.isWord = isWord
        self.children = {}
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        trie = self.root
        n = len(word)
        for i in range(n):
            let = word[i]
            if let not in trie.children:
                trie.children[let] = TrieNode()
            if i == n-1:
                trie.children[let].isWord = True
            trie = trie.children[let]
                

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        trie = self.root
        n = len(word)
        for i in range(n):
            if word[i] in trie.children:
                trie = trie.children[word[i]]
            else:
                return False
        return trie.isWord

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        trie = self.root
        n = len(prefix)
        for i in range(n):
            if prefix[i] in trie.children:
                trie = trie.children[prefix[i]]
            else:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
