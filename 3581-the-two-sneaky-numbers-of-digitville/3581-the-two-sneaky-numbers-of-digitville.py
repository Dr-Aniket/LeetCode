class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        def count(n):
            return nums.count(n)

        return sorted(set(nums), key = count,reverse=True)[:2]
