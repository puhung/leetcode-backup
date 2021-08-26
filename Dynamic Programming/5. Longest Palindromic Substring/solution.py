class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def maxPaliLen(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            #since after the loop, left would be smaller  by 1 and right would be larger by 1
            #left and right are all not we want
            # left, substring ..., right => len of the pali string right - left + 1 - 2
            return right - left - 1
        
        start, length = 0, 0

        for i in range(n):

            #calculate the max pali length (even and odd) start from the substing middle index i
            #move from inside to outside
            tempMaxLen = max(maxPaliLen(i, i), maxPaliLen(i, i+1)) 

            if tempMaxLen <= length: 
                continue
            # update and store the length and start point            
            length = tempMaxLen
            start = i - (tempMaxLen - 1) // 2 #  (tempMaxLen - 1) because: for odd length array, the start point of the array is still i
        
        return s[start: start + length]