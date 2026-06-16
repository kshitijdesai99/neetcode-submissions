class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins = []
        minz = float("inf")
        for i in prices:
            minz = min(minz,i)
            mins.append(minz)

        maxs = []
        maxz = float("-inf")
        for i in prices[::-1]:
            maxz = max(maxz,i)
            maxs.append(maxz)

        maxs = maxs[::-1]

        total_profit = 0
        for i in range(len(prices)):
            total_profit = max(total_profit, maxs[i]-mins[i])

        return total_profit