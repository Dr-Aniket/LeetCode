class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        if len(timePoints) != len(set(timePoints)):
            return 0
        def make_minutes(tym:str):
            hours,minutes = tym.split(':')
            return int(hours)*60 + int(minutes)

        timePoints = list(map(make_minutes,timePoints))
        timePoints.sort()

        size = len(timePoints)
        
        Min = None
        for i in range(size):
            diff = abs(timePoints[(i+1)%size]-timePoints[i])
            if diff > 12*60:
                diff = 24*60 - diff
            if Min == None:
                Min = diff
            elif diff < Min:
                Min = diff
                
        return Min