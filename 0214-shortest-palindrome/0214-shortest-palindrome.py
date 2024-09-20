class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        append_at = 0
        invert_s = s[::-1]
        for c in invert_s:
            if s == s[::-1]:
                return s
            else:
                s = s[:append_at] + c + s[append_at:]
                append_at += 1


        
        