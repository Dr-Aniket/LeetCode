class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = 10**5+1
        price = 0

        for p in prices:
            if p<smallest:
                smallest = p
            else:
                if p-smallest > price:
                    price = p-smallest
        return price