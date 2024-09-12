class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        map = {}

        for i,j in zip(pattern,s):
            if i in map:
                if map[i] != j:
                    return False
            else:
                map[i] = j
        
        map = {}

        for i,j in zip(s,pattern):
            if i in map:
                if map[i] != j:
                    return False
            else:
                map[i] = j
        
        return True