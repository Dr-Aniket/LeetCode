class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return sorted(set(nums), key = lambda a: nums.count(a))[-2:]
