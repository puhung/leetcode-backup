class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0

        rows = len(matrix) 
        cols = len(matrix[0])

        # use dp to store the longest sqaure length in that position
        dp = [[0] * (cols + 1) for r in range(rows + 1)]
        max_side = 0

        #since we need to look up the element in matrix, r and c can not be larger than rows and cols
        #Thus r and c must start from 0 to rows-1 instead of start from 1 to rows 
        for r in range(rows):
            for c in range(cols):
                
                if matrix[r][c] == "1":
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    max_side = max(max_side, dp[r][c])

        return max_side * max_side