class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums,key = lambda a: a%2 != 0)