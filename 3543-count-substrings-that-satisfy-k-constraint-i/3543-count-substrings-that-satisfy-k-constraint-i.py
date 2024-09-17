class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        def valid(string):
            return string.count('1') <= k or string.count('0') <= k 
        
        return sum(1 for i in range(len(s)) for j in range(i+1,len(s)+1) if valid(s[i:j]) )
