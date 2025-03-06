class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_elements = n * n
        
        # Expected sum and sum of squares
        expected_sum = (total_elements * (total_elements + 1)) // 2
        expected_sum_sq = (total_elements * (total_elements + 1) * (2 * total_elements + 1)) // 6
        
        actual_sum = 0
        actual_sum_sq = 0
        num_counts = {}
        
        # Compute actual sum and sum of squares
        for row in grid:
            for num in row:
                actual_sum += num
                actual_sum_sq += num * num
                num_counts[num] = num_counts.get(num, 0) + 1
        
        # Find the repeating number
        for key, value in num_counts.items():
            if value == 2:
                a = key  # Repeated number
                break
        
        # Compute missing number using derived formulas
        b = a + (expected_sum - actual_sum)
        
        return [a, b]