class Solution:
    def minimumSteps(self, s: str) -> int:
        # steps = 0
        # s = list(s)
        # for i in range(len(s)):
        #     for j in range(0,len(s)-1):
        #         if s[j] == '1' and s[j+1] == '0':
        #             s[j], s[j+1] = s[j+1], s[j]
        #             steps += 1

        # return steps

        steps = 0
        prev1 = 0
        for c in s:
            if c == '0':
                steps += prev1
            else:
                prev1 += 1
        
        return steps
