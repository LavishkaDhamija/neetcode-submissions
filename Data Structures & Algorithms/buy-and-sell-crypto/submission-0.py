class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1 = float('inf')
        max_profit = 0
        for i in prices:
            if i < min1:
                min1 = i
            max_profit = max(max_profit,i-min1)

        return max_profit

        