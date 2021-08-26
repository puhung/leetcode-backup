# MORE BETTER SOLUTION!!!
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                if word == s[i - len(word) + 1 : i + 1] and (dp[i - len(word)] or i - len(word) == -1):
                    dp[i] = True
        return dp[-1]

#solution 2
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # the map to store whether the string is in the wordDict or not
        map = {}

        def canBreak(str):
            if str in map:
                return map[str]
            if str in wordDict:
                map[str] = True
                return True
            
            # since the base case has already checked whether str is in wordDict
            # we can start seperate the str from index 1 
            for i in range(1, len(str)):
                seperate = str[i:]
                if seperate in wordDict and canBreak(str[0:i]):
                    map[str] = True
                    return True
            
            map[str] = False
            return False
        
        return canBreak(s)

