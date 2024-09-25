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
    
    def get_prefix_score(self, word: str) -> int:
        node = self.root
        score = 0
        for char in word:
            if char in node.children:
                node = node.children[char]
                score += node.prefix_count
            else:
                break
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Initialize Trie
        trie = Trie()
        
        # Insert all words into the Trie
        for word in words:
            trie.insert(word)
        
        # Calculate the sum of prefix scores for each word
        result = []
        for word in words:
            result.append(trie.get_prefix_score(word))
        
        return result
