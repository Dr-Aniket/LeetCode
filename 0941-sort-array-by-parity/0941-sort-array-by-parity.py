class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            if nums[i]%2 == 0:
                ans.append(nums[i])
                nums.remove(nums[i])
            else:
                i += 1
        return ans + nums
