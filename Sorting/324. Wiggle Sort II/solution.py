class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2]) #we want Odd-index numbers to be larger than their neighbors. Thus, half would help us pick more small numbers than larger numbers to fit in the odd-index

        #even number, odd number 
        nums[::2], nums[1::2] = nums[:half][::-1] , nums[half:][::-1]