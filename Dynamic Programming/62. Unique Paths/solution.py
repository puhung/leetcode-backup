class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #create a m * n array with all value equals to 1
        #[[1,1,1,1,1...], [1,1,1,1,1...], [1,1,1,1,1...], [1,1,1,1,1...] ...]
        res = [[1]*n]*m 

        #start from 1 row since m >= 1
        for i in range(1, m):
             #start from 1 column since n >= 1
            for j in range(1, n):
                # curr = top + left
                res[i][j] = res[i-1][j] + res[i][j-1]
            
        return res[m-1][n-1]


#better solution 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #create an array with n value equals to 1
        res = [1]*n 

        #start from 1 row since m >= 1
        for i in range(1, m):
            #start from 1 column since n >= 1
            for j in range(1, n):
                # curr = top + left 
                # res[j] represents the top element, res[j-1] represents the left element
                res[j] = res[j-1] + res[j]
            
        return res[-1]


