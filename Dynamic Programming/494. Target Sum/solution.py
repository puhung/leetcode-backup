class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        idx = len(nums) - 1
        curr_sum = 0       
        memo = {}
        return self.dp(nums, target, idx, curr_sum, memo)

    def dp(self, nums, target, idx, curr_sum, memo):
            #base case
            if (idx, curr_sum) in memo:
                return  memo[(idx, curr_sum)]
            if idx < 0 and curr_sum == target:
                return 1
            if idx < 0:
                return 0
            
            #Decisions
            positive = self.dp(nums, target, idx - 1, curr_sum + nums[idx])
            negative = self.dp(nums, target, idx - 1, curr_sum - nums[idx])

            memo[(idx, curr_sum)] = positive + negative
            return memo[(idx, curr_sum)]
        
