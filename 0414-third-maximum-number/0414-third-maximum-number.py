class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        return nums[-1] if len(nums)<3 else nums[-3]