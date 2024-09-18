class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda a: a**2,nums))