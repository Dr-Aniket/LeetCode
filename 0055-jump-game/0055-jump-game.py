class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1 or 0 not in nums:
            return True
        
        zero_indexes = [i for i in range(n) if nums[i]==0]

        for zero_index in zero_indexes:
            for i, val in enumerate(nums[:zero_index]):
                if zero_index == n-1:
                    if i+val >= zero_index:
                        break
                else:
                    if i+val > zero_index:
                        break
            else:
                return False

        return True
