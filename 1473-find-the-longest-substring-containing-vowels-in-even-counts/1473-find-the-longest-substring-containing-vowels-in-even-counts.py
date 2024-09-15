class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def isEven(string):
            return string.count('a')%2==0 and  string.count('e')%2==0 and  string.count('i')%2==0 and string.count('o')%2==0 and  string.count('u')%2==0
                       
        max_len = len(s)

        for size in range(max_len,0,-1):
            for j in range(0,max_len - size + 1):
                if isEven(s[j:j+size]):
                    return size
        return 0