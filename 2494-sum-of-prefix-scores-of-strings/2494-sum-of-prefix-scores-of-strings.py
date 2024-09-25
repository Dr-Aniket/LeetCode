from collections import defaultdict
from typing import List

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Dictionary to store the frequency of each prefix
        prefix_count = defaultdict(int)
        
        # First, count how many words have each prefix
        for word in words:
            prefix = ""
            for char in word:
                prefix += char
                prefix_count[prefix] += 1
        
        # Now, calculate the sum of prefix scores for each word
        result = []
        for word in words:
            prefix = ""
            total_score = 0
            for char in word:
                prefix += char
                total_score += prefix_count[prefix]
            result.append(total_score)
        
        return result
