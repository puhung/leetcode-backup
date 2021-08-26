class Solution:
    def numDecodings(self, s: str) -> int:
        # we use this dict to store the decode ways of each position
        # "len(s): 1" is teh base case, which is the decode way of the last element: 1
        decodeDict = {len(s): 1}

        # we loop backward from the last element to the first element at index 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                decodeDict[i] =  0
            else:
                # for example: "226"

                # this is the first case where we see s[i] (2) as a seperate element 
                # then its decode ways would be the decode ways of the rest of string
                # which is decodeDict[i + 1]  (26)
                decodeDict[i] = decodeDict[i + 1]  

            #the second case
            # we see s[i] and s[i+1] as a group (22), then its decode ways would be decodeDict[i + 2] (6)
            # i + 1 must be in the string to check second case
            if ((i + 1 < len(s)) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")) :
                decodeDict[i] += decodeDict[i+2]
        return decodeDict[0]

#recursion
class Solution:
    def numDecodings(self, s: str) -> int:

        decodeDict = {len(s): 1}

        def dfs(i):
            if i in decodeDict:
                return decodeDict[i]
            if s[i] == "0":
                return 0

            decodeDict[i] = dfs(i+1)

            if ((i + 1 < len(s)) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")) :
                decodeDict[i] += dfs(i+2)
            
            return decodeDict[i]
        return dfs(0)

