class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, key = lambda a: a%2 != 0 )
        ans = []
        for i in range(len(nums)//2):
            ans.append(nums[i])
            ans.append(nums[-i-1])
        
        return ans
            