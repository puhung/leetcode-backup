class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        robDP = [0] * len(nums)
        robDP[0] = nums[0]
        robDP[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            robDP[i] = max(robDP[i-1], nums[i] + robDP[i-2])
        
        return robDP[-1]
    
#Better solution with small space complexity
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        prev = 0
        curr = 0

        for num in nums:
            temp = prev
            prev = curr
            curr = max(prev, num + temp)
        
        return curr