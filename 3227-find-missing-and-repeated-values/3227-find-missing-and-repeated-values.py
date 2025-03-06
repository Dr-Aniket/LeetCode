class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)**2
        actual_sum = (n*(n+1))//2
        pre = []

        for row in grid:
            for ele in row:
                if ele in pre:
                    rep = ele
                pre.append(ele)
        
        return [rep, rep + actual_sum-sum(pre)]