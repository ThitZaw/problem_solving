class Solution:
    def maxProfit(self, prices):
        buy_price = prices[0]
        profit = 0
        for day in range(1,len(prices)):
            if prices[day] < buy_price:
                buy_price = prices[day]
            profit = max(profit,prices[day]- buy_price)
        return profit

sol = Solution()
sol.maxProfit([7,1,5,3,6,4])        