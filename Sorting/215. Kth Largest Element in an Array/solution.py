class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        #[LEFT...][mid...][right...]
        #the kth largest element is inside left
        if k <= len(left):
            return self.findKthLargest(left, k)
        #the kth largest element is inside right
        elif k > len(left) + len(mid):
            return self.findKthLargest(right, k-(len(left) + len(mid)))
        else:
            return mid[0]

