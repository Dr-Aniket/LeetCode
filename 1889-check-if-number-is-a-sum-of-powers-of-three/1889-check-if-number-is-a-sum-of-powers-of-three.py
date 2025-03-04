class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = int(n**(1/3))

        s = 0

        while i>=0 :
            p = 3**i
            if s+p < n:
                s += p
            elif s+p == n:
                return True          
            i -= 1
        
        return False
