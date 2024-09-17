class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return not (sum(i for i in nums if i < 10 ) == sum(i for i in nums if i > 9 ))
            