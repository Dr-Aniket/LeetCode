class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri = []
        for i in range(1,rowIndex+2):
            row = []
            for j in range(i):
                if j == 0:
                    row.append(1)
                elif j == i-1:
                    row.append(1)
                    break
                else:
                    row.append(tri[-1][j-1]+tri[-1][j])
            tri.append(row)

        return tri[-1]