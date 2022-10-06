class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        buy_price = prices[0]
        for day in range(1,len(prices)):
            maxprofit = max(maxprofit,prices[day]-buy_price)
            buy_price = min(buy_price,prices[day])
        return maxprofit