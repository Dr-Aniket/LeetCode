class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        elif len(s1) != len(s2):
            # print('there false')
            return False
        
        n = len(s1)

        diff = 0

        check_char1 = ''
        check_char2 = ''         

        for i in range(n):
            c1 = s1[i]
            c2 = s2[i]

            if c1 != c2:
                diff += 1
            
            if diff == 1 and not check_char1:
                check_char1 = c1
                check_char2 = c2
                # print(f'Check11 = {check_char1} | Check22 = {check_char2} | ')

            elif diff == 2:
                if not (check_char1 == c2 and check_char2 == c1):
                    # print(f'here fasle')
                    # print(f'Check1 = {check_char1} | Check2 = {check_char2} | ')
                    # print(f'c1 = {c1} | Check2 = {c2} | ')
                    return False
                else:
                    return s1[i+1:] == s2[i+1:]
        
        return False