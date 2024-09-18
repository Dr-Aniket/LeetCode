from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all integers to strings
        nums_str = list(map(str, nums))
        
        # Define a custom comparator for sorting
        def compare(x, y):
            # Compare concatenated results of x+y and y+x
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Concatenate all numbers
        largest_number = ''.join(nums_str)
        
        # Handle the case where the result is '0' (e.g., [0, 0])
        return largest_number if largest_number[0] != '0' else '0'
