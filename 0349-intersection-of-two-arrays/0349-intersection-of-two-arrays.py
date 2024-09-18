class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
   
        if len(nums1) > len(nums2):
            temp = nums1.copy()
            nums1 = nums2.copy()
            nums2 = temp
        
        return set(i for i in nums1 if i in nums2)
                