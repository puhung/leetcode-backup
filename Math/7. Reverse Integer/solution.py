class Solution:
    def reverse(self, x: int) -> int:
        
        sign = [1,-1][x<0] # x <0 == true, sign == [1,-1][1]

        res = sign * int(str(abs(x))[::-1])

        return res if  -2**31 <= res <= 2**31 - 1 else 0