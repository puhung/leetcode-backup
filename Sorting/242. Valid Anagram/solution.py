class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}

        if len(s) != len(t):
            return False

        for item in s:
            if item not in counter:
                counter[item] = 1
            else:
                counter[item] += 1
        for item in t:
            if item in counter:
                counter[item] -= 1
            else: 
                return False
        
        # for item in counter:
        #     if counter[item] != 0:
        #         return False
        for value in counter.values():
            if value != 0:
                return False
            
        return True

#solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2