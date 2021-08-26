class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x == 0:
            return 0

        left, right = 0, x
        
        while left <= right:
            mid = left + (right-left)//2 # to avoid overflow of adding 2 large integers

            if mid ** 2 <= x < (mid + 1)**2:
                return mid
            elif mid ** 2 > x:
                right = mid - 1            
            else:
                left = mid + 1

