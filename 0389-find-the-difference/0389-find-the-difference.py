class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i,j in zip(s,t):
            if i != j:
                return j
        else:
            return t[-1]
