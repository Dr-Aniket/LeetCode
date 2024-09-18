class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            ele = nums[i]
            if ele%2 == 0:
                ans.append(ele)
                nums.remove(ele)
            else:
                i += 1
        return ans + nums
