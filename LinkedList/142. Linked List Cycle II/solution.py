class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None
        
        pointer = head
        while pointer != fast:
            pointer = pointer.next
            fast = fast.next
        
        return pointer
        