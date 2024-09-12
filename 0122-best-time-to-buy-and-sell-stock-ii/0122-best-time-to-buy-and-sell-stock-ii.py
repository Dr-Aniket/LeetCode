class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0
        for i,j in zip(prices[:-1],prices[1:]):
            if j-i > 0:
                price += j-i
        return price