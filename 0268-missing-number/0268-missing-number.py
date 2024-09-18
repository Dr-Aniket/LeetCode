class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[-1]+1
        for i in range(n):
            if nums[i] != i:
                return i
        else:
            return n