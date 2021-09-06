class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        citations.reverse()

        res = 0

        for idx in range(len(citations)):
            if citations[idx] >= (idx + 1):
                res = idx + 1
            else:
                return res

        return res
            