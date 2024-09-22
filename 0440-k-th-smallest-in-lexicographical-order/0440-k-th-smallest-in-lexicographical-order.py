class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Function to calculate how many numbers exist between the prefix and n
        def count_steps(prefix, n):
            steps = 0
            first = prefix
            last = prefix
            while first <= n:
                steps += min(n + 1, last + 1) - first
                first *= 10
                last = last * 10 + 9
            return steps
        
        current = 1
        k -= 1  # We start at the first number, so reduce k by 1

        while k > 0:
            steps = count_steps(current, n)
            if steps <= k:
                # If the steps under the current prefix are fewer than or equal to k,
                # we skip this prefix and move to the next one
                current += 1
                k -= steps
            else:
                # Otherwise, we go deeper in this prefix (multiply by 10)
                current *= 10
                k -= 1

        return current
