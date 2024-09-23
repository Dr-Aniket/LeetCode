class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        # Initialize dp array with maximum values (extra characters)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1  # Assume the current character is an extra one
            # Try to match all substrings ending at index i-1
            for j in range(i):
                if s[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])  # No extra characters added if it's a valid word
        
        return dp[n]
