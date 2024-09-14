class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        c = 0
        MAX = 0
        for ele in nums:
            if ele == m:
                c += 1
            else:
                if c >= MAX:
                    MAX = c
                c = 0
            
        return max(MAX,c)
        