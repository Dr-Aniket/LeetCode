class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^a-z0-9]','',s.lower())

        return s==s[::-1]