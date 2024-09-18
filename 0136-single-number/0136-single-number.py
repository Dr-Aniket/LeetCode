class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return eval('^'.join(map(str,nums)))