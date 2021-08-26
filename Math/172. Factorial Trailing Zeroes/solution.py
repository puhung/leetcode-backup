class Solution:
    def trailingZeroes(self, n: int) -> int:
        #we would find the number of integer that contains one 5, then find the number of integer that contains two 5, etc
        return  0 if n == 0 else int(n/5) + self.trailingZeroes( int(n/5))
    
#solution 2
class Solution:
    def trailingZeroes(self, n: int) -> int:
        sum = 0
        while n > 0:
            n = n // 5
            sum += n
        return sum 