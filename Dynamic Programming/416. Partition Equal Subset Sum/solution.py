class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for n in nums:
            newDp =set()
            for eachSum in dp:
                if eachSum + n == target: 
                    return True
                newDp.add(eachSum)
                newDp.add(eachSum + n)
            dp = newDp
        
        return target in dp
            
        