class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3: 
            return len(nums)
        slow = fast = 2

        while fast < len(nums):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow 

#solution 2

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0 or not nums: return 0

        idx = 0
        dup = False
        originalLength = len(nums)

        while idx < len(nums) - 1:
            if nums[idx] == nums[idx + 1]:
                if not dup:
                    dup = True
                else:
                    nums.pop(idx)
                    idx -= 1
            else:
                dup = False

            idx += 1

        res = len(nums)
        nums.extend([None] * (originalLength - res))

        return res

