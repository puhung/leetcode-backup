# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow= slow.next
            fast = fast.next.next

        #reverse the second half of the list
        prev, curr = None, slow.next
        while curr:
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next
        #prev would be the head of the second half of the list

        # avoid a list with loop. Disconnect the first half from the second half
        slow.next = None 

        #reorder the list
        head1, head2 = head, prev

        #head2 would always be the last node in the reordered list
        while head2:
            next = head1.next
            head1.next = head2
            head1 = head2
            head2 = next
     
#faster solution
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if head is None:
            return
        
        #slow and fast pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #be careful where middle stops
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next
            
        first = head 
        second = pre
        
        while second.next:
            tmp1 = first.next
            first.next = second
            tmp2 = second.next
            second.next = tmp1
            first = tmp1
            
