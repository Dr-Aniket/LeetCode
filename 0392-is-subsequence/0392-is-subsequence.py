class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # import re
        # return re.search('.*'.join(s),t)
        for c in s:
            try:
                i = t.index(c)
                t = t[i+1:]
            except:
                return False
        
        return True