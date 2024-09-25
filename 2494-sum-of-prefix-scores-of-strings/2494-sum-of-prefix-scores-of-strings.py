from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Initialize Trie
        trie = Trie()
        
        # Insert all words into the Trie
        for word in words:
            trie.insert(word)
        
        # Calculate the sum of prefix scores for each word in a single traversal
        result = []
        for word in words:
            node = trie.root
            total_score = 0
            for char in word:
                node = node.children[char]
                total_score += node.prefix_count
            result.append(total_score)
        
        return result
