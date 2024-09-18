class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[-1] > 0:
            return  nums[-1] * max(nums[0]*nums[1],nums[-2]*nums[-3])
        else:
            return  nums[-1] * min(nums[0]*nums[1],nums[-2]*nums[-3])