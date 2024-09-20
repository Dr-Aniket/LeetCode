class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        s = list(s)
        append_at = 0
        for c in s[::-1]:
            if s == s[::-1]:
                return ''.join(s)
            else:
                s.insert(append_at,c)
                append_at += 1
        

        
        