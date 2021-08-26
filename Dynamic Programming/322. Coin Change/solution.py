class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[i] is the fewest number of coins making up amount i
        # i starts from 0 to amount
        dp = [0] + [float("inf") for i in range(amount)]

        for num in range(1, amount + 1):
            for coin in coins:
                if num - coin >= 0:
                    dp[num] = min(dp[num], 1 + dp[num - coin])
        
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]