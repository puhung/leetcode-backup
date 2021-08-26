class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        
        # use a dp to store the min number of perfect square number to sum up to each number from 0 to n
        # the worst case is n, since n = 1+1+1+1...
        #there is n + 1 numbers from 0 to n
        dp = [n] * (n+1)
        dp[0] = 0

        for num in range(1, n+1):
            for s in range(1, num+1):
                square = s * s
                if num - square < 0:
                    break # ex: 12 - 4^2 <0
                
                # ex: 12 - 2 ^ 2 = 8 => the number of perfect square number to sum up to 12 = 1 + dp[8]
                dp[num] = min(dp[num], 1 + dp[num - square])

        return dp[n]