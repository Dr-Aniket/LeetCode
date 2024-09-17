class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        if sum(i for i in nums if i < 10 ) == sum(i for i in nums if i > 9 ):
            return False
        return True
        