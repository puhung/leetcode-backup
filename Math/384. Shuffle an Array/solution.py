class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """        
        return self.array
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = []
        res = self.array[:]
        for i in range(len(self.array)):
            randomNum = random.randrange(i, len(self.array))
            res[i], res[randomNum] = res[randomNum], res[i]
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()