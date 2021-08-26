class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # we use defaultdict because the count key may not exist 

        for s in strs:
            count = [0] *26

            for char in s: 
                count[ord(char) - ord("a")] += 1 #record each char into the count array. ord() is the number specify for the char

            res[tuple(count)].append(s) #group the strings that has the same count together. Also since list can not be key, we need to change it into a tuple

        return res.values()