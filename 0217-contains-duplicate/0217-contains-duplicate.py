class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return sorted(set(nums)) != sorted(nums)