class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bin_start = str(bin(start))[2:]
        bin_goal = str(bin(goal))[2:]

        Max = max(len(bin_start),len(bin_goal))

        bin_start = (Max-len(bin_start))*'0' + bin_start
        bin_goal = (Max-len(bin_goal))*'0' + bin_goal

        count = 0
        for i in range(Max):
            if bin_goal[i] != bin_start[i]:
                count += 1
        
        return count