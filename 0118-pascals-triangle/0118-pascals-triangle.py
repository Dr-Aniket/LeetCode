class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for i in range(1,numRows+1):
            row = []
            for j in range(i):
                if j == 0:
                    row.append(1)
                elif j == i-1:
                    row.append(1)
                    break
                else:
                    prev_row = tri[-1]
                    row.append(prev_row[j-1]+prev_row[j])
            tri.append(row)

        return tri
