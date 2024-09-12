class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def count(lst):
            c = {}
            for i in lst:
                if i in c:
                    c[i] += 1
                else:
                    c[i] = 1
            return c
        
        ransomNote = count(ransomNote)
        magazine = count(magazine)

        for n in ransomNote:
            if n not in magazine:
                return False
            magazine[n] -= ransomNote[n]
            if magazine[n] < 0:
                return False
        
        return True
        