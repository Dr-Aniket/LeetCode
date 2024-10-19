class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(x):
            new_x = ''
            for i in x:
                if i == '0':
                    new_x += '1'
                else:
                    new_x += '0'
            return new_x

        if k == 1:
            return '0'
        s = '0'

        while len(s) < k:
            s += '1' + invert(s)[::-1]

        return s[k-1]