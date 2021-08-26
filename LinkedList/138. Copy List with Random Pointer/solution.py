"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        #edge case: the curr.next or curr.random == None. Thus, we need to define a None: None key-value pair first
        dic = {None: None}
        
        curr = head
        while curr:
            copy = Node(curr.val) # the next and random pointers aren't assigned yet
            dic[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = dic[curr]
            copy.next = dic[curr.next]
            copy.random = dic[curr.random]
            curr = curr.next

        return dic[head]
            
