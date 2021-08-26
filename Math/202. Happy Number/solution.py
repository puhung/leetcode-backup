class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        #if n is in visited, this means that n would be in a endless loop without becoming 1.
        #Thus, if we saw repeated n in visited, we can return false
        while n not in visited :
            visited.add(n)
            n = self.sumOfSquare(n)

            if n == 1:
                return True
        return False

    def sumOfSquare(self, n):
        newN = 0
        while n:
            #ex: n = 19
            digit = n % 10 #digit = 9
            newN += digit ** 2 # newN +=  9**2
            n = n // 10 # n = 1
        return newN
