class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        ans = []
        pre = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] in pre:
                    ans.append(grid[i][j])
                else:
                    pre.append(grid[i][j])
        
        pre.sort()

        for i, ele in enumerate(pre+[0]):
            if i+1 != ele:
                ans.append(i+1)
                break
        
        return(ans)