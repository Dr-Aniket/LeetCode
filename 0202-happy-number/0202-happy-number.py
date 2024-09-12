class Solution:
    def isHappy(self, n: int) -> bool:
        pre_done = []

        def happy(n,pre_done):
            if n == 1:
                return True
            elif n in pre_done:
                return False
            else:
                pre_done.append(n)
                            
            return happy(sum([int(i)**2 for i in str(n)]),pre_done)
        
        return happy(n,pre_done)