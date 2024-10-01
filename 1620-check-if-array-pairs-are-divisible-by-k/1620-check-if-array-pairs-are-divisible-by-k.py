class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = defaultdict(int)

        # Count the remainders
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1

        # Check pairs
        for rem in list(remainder_count):
            # Special case for remainder 0, there must be an even number of such elements
            if rem == 0:
                if remainder_count[rem] % 2 != 0:
                    return False
            # Special case for remainder k/2 when k is even, there must be an even number of such elements
            elif k % 2 == 0 and rem == k // 2:
                if remainder_count[rem] % 2 != 0:
                    return False
            else:   
                # For other remainders, the number of elements with remainder 'rem' must match
                # the number of elements with remainder 'k - rem'
                if remainder_count[rem] != remainder_count[k - rem]:
                    return False
        
        return True