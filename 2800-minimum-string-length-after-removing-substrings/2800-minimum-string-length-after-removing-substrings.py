class Solution:
    def minLength(self, s: str) -> int:
        i = 0
        subs = ['AB','CD']
        while True:
            if not (subs[0] in s or subs[1] in s):
                break

            s = s.replace(subs[i],'')
            i = (i+1)%2
        
        return len(s)