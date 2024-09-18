class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        positions = sorted(score,reverse = 1)
        def place(i):
            i = positions.index(i) + 1
            if i == 1:
                return 'Gold Medal'
            elif i == 2:
                return 'Silver Medal'
            elif i == 3:
                return 'Bronze Medal'
            else:
                return str(i)

        return list(map(place,score))