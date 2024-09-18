class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return list(map( lambda a: a**2,sorted(nums,key = abs) ) )