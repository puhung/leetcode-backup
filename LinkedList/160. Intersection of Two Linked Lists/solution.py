# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        a = headA
        b = headB
        while a != b:
            a = headB if not a else a.next
            b = headA if not b else b.next

        #return the intersected node
        return a

#solution2
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dict = {}
        a = headA
        b = headB

        while(a):
            dict[a] = a.val
            a = a.next
        while(b):
            if b in dict:
                #return the intersected node
                return b
            b = b.next
        return None