# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:        

        if not head or not head.next:
            return head

        left = head
        right = self.getMid(head)

        #separate the list into 2 half
        temp = right.next
        right.next = None
        right = temp

        #repeat separating the sublist until each sublist only contains 1 node
        left = self.sortList(left)
        right = self.sortList(right)

        #merge + sort left and right into a complete list
        return self.mergeList(left, right)

    def getMid(self, head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

    def mergeList(self, list1, list2):
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next #update curr

        if list1: 
            curr.next = list1
        if list2:
            curr.next = list2
            
        return dummy.next        

        



