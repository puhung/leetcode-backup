class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [0] * len(nums)

        # DP definition: The farthest index we can reach with all the steps from 0 to i
        dp[0] = nums[0]

        #we only need to loop til the last 2 element and check whether that position can reach (length - 1) or not
        for i in range(1, len(nums)):

            #chack if nums[i-1] is 0
            #because if nums[i-1] is bigger than 0, it can at least reach i by (i-1) + 1
            if dp[i - 1] < i:
                return False
            
            dp[i] = max(dp[i-1], i + nums[i])

            if dp[i] >= len(nums) - 1:
                return True

        #check if last 2 element can reach the last element or not
        return dp[len(nums)-2] >= len(nums) - 1

#solution 2
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums) -1

        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] + i) >= last_position:
                last_position = i
        return last_position == 0