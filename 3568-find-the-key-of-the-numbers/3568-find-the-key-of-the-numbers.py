class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 = '0'*(4-len(str(num1))) + str(num1)
        num2 = '0'*(4-len(str(num2))) + str(num2)
        num3 = '0'*(4-len(str(num3))) + str(num3)

        key = ''
        for i,j,k in zip(num1,num2,num3):
            key += str(min(map(int,[i,j,k])))

        return int(key)