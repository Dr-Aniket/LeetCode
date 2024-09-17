class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        def count(n):
            return nums.count(n)

        nums = sorted(set(nums), key = count,reverse=True)

        return nums[:2]
