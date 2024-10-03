class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total % p == 0:
            return 0
        if total < p:
            return -1
        target = total % p
        prefix = 0
        prefix_sum = {0: -1}
        min_len = n
        for i in range(n):
            prefix = (prefix + nums[i]) % p
            prefix_sum[prefix] = i
            if (prefix - target) % p in prefix_sum:
                min_len = min(min_len, i - prefix_sum[(prefix - target) % p])
        return min_len if min_len < n else -1
    