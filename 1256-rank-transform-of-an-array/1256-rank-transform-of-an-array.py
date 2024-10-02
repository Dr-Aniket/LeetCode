class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Sort the array and remove duplicates
        sorted_unique = sorted(set(arr))
        
        # Step 2: Create a dictionary to map each element to its rank
        rank_dict = {num: rank + 1 for rank, num in enumerate(sorted_unique)}
        
        # Step 3: Replace each element in the original array with its rank
        return [rank_dict[num] for num in arr]
