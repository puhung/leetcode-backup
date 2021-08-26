# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # ex: head = [1,2,3,4,5], n = 2

        def index(node):
            if node is None:
                return 0
            idx = index(node.next) + 1
            
            #move the value of the current node to its next position
            if idx > n:
                node.next.val = node.val

            return idx

        index(head)
        # we return head.next because the head still exist
        #after modification, the head = [1,1,2,3,5], the idx of the listnode: [5,4,3,2,1]
        return head.next
        
#solution2:
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        #move fast n steps forward
        for _ in range(n):
            fast = fast.next
        
        # 1 <= n <= sz (The number of nodes in the list)
        # special case: when n is exactly equal to sz, which means the head is the node we want to remove
        if not fast:
            return head.next
        
        #move the slow right in the position before the node we want to remove
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        # remove the node by setting the next node of the node before the target to the next node of the target 
        slow.next = slow.next.next

        return head
        

