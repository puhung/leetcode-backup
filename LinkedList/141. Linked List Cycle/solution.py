# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
            
        slow = head
        fast = head.next

        while slow != fast:
            # not endless loop
            # we need to check the condition first, since if fast doesn't initially have next, we can not find fast.next.next. THus causing error
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next  

        # if there is a cycle, the pointers would meet and stop the loop 
        return True

#solution2
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
            
        slow = fast = head
        while fast and fast.next:            
            slow = slow.next
            fast = fast.next.next

            #since we initially set slow = fast, thus we need to assign slow and fast into a new value, then we check the condition
            if fast == slow:
                return True

        return False

        