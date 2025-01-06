class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls = [i for i in range(len(boxes)) if boxes[i]=='1']
        
        answer = []

        for i in range(len(boxes)):
            answer.append( sum( [abs(ball-i) for ball in balls] ) )

        return answer