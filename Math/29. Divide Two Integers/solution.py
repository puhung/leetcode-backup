class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isPositive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        res = 0

        #keep looping until dividend <= divisor
        while dividend >= divisor:
            currDivisor, i = divisor, 1

            # To fast the process, we multiple the currdivisor by 2
            # If currdivisor > dividend, we restart the process
            while currDivisor <= dividend:
                dividend -= currDivisor
                res += i

                #Since we can not use *, we use bit manipulation
                i <<= 1 # i = i * (2^1)
                currDivisor <<= 1 # currDivisor = currDivisor * (2^1)
        
        if not isPositive:
            res = -res

        return res if res in range(-2147483648, 2147483648 - 1 ) else 2147483648 -1