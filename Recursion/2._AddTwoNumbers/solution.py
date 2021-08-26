class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Since we don't know what first value in our list would be. Thus, we use dummy head. It is just a place holder, so that we can attach other values to. Add at the ending, we could return whatever is the next of the dummy node.
        dummy = ListNode(0)
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum_val = l1_val + l2_val + carry
            curr.next = ListNode(sum_val % 10) # we only want the remainder

            #update pointers and value
            carry = sum_val // 10 # // is 整數除法
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
