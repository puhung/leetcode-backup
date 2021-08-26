class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        res = 1
        
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
                    res = max(res, dp[i])
        return res
