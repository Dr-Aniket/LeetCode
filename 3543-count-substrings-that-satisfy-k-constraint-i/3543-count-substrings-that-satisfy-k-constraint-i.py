class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        def valid(string):
            return string.count('1') <= k or string.count('0') <= k 
        
        count = 0
        for size in range(1,len(s)+1):
            for i in range(0,len(s)-size+1):
                if valid(s[i:i + size]):
                    count += 1

        return count 