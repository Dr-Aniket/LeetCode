class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = (s1 + ' ' + s2).split()

        count = {}
        for word in s:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
        
        return [word for word in count if count[word] == 1]
