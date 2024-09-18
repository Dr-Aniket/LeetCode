class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sorted(nums,key=lambda a: nums.count(a))[0]