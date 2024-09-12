class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return sum([prices[i+1] - prices[i] for i in range(0,len(prices)-1) if  prices[i+1] - prices[i] > 0])

        price = 0
        for i,j in zip(prices[:-1],prices[1:]):
            if j-i > 0:
                price += j-i
        return price