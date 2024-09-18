class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums2 = sorted(nums)

        if nums2[-1] >= nums2[-2]*2:
            return nums.index(nums2[-1])
        else:
            return -1