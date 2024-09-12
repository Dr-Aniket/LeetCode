class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        MAP = {}
        for i,j in zip(s,t):
            if i in MAP:
                if j != MAP[i]:
                    return False
            else:
                MAP[i] = j
        
        MAP = {}
        for i,j in zip(t,s):
            if i in MAP:
                if j != MAP[i]:
                    return False
            else:
                MAP[i] = j
        
        return True
