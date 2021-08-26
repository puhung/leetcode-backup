class Solution:
    
    def largestNumber(self, nums: List[int]) -> str:

        #if every number in nums is 0(false), return '0'
        if  not any(map(bool, nums)):
            return '0'

        #since our return type is string, convert input into string first
        nums = list(map(str, nums))
        if len(nums) < 2:
            return ''.join(nums)   
        
        #compare the 2 concat strings
        def compare(x, y):
            return int(nums[x] + nums[y]) > int(nums[y] + nums[x])   
                    
        # compare and swap
        for x in range(len(nums) - 1):
            y = x+1
            while x < len(nums) and y < len(nums):
                #if x+y > y+x don't swap
                if compare(x,y):
                    pass
                else: 
                    nums[y], nums[x] = nums[x], nums[y]
                # move y and compare the current x and new y
                y += 1
        #the join method can only concat string type
        return ''.join(nums)

#solution2
class largerNum(str):
    def __lt__(x,y):
        return x+y > y+x
class Solution:
    
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=largerNum))
        return  '0' if largest_num[0] == '0' else largest_num