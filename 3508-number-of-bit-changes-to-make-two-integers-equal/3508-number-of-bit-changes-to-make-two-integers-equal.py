class Solution:
    def minChanges(self, n: int, k: int) -> int:
        bin1 = bin(n)[2:]
        bin2 = bin(k)[2:]

        m = max(len(bin1),len(bin2))

        bin1 = '0'*(m-len(bin1)) + bin1
        bin2 = '0'*(m-len(bin2)) + bin2
    
        c = 0
        for i,j in zip(bin1,bin2):
            if i != j:
                if i == '0':
                    return -1
                else:
                    c += 1

        return c   
                