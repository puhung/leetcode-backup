#This class used to set the key-value pairs as nodes in LRU object
from typing import OrderedDict


class LinkedListNode(object):
    def __init__(self, key = None, val = -1):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def appendHead(self, node):
        node.next, node.pre = self.head, None

        if self.head:
            self.head.pre = node
        
        self.head = node

        if not self.tail:
            self.tail = self.head

        self.size += 1

    def remove(self, node):
        pre, next = node.pre, node.next

        if pre:
            pre.next = node.next        
        if next:
            next.pre = node.pre
        
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.pre

        self.size -= 1        
        return node

    def removeTail(self):
        #remove the LRU
        return self.remove(self.tail)
    
    def combination(self, node):
        #when we get the value, we need to adjust the order of the list, to make sure LRU is correct
        self.remove(node)
        self.appendHead(node)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {} #store the node as value into the dict[key]
        self.linkedList = LinkedList() # The order of the recently used node would be store in this list and the least recently used node will be at the tail of the dict

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        else:
            self.linkedList.combination(self.dict[key])
            return self.dict[key].val


    def put(self, key: int, value: int) -> None:       

        if key in self.dict:
            #since there is key in the dict, we dont need to convert the key-value into a node
            self.dict[key].val = value # update the value of the node, which is the value of the key
            self.linkedList.combination(self.dict[key]) # Since we use this node, we need to update it as the Least Recently Used
        
        else:
            node = LinkedListNode(key, value) # first set the key-value into a node

            self.linkedList.appendHead(node)
            self.dict[key] = node # dict = { key: linkedListNode(key, node)}

            # Since the linkedlist has the same size as dict, we can use it to check if dict is full.
            if self.linkedList.size > self.capacity:
            
                del self.dict[self.linkedList.removeTail().key]
                

# orderdict solution
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1  
        else:
            
            # utilize the poperty of ordereddict: when item is popped and added again, its order in the ordereddict would change.
            value = self.dict.pop(key)
            self.dict[key] = value

            return value

            #we can also achieve the goal by:
            #self.cache.move_to_end(key)  # Gotta keep this pair fresh, move to end of OrderedDict
            #return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key) 
            self.dict[key] = value

            # this equals:
            #self.cache.move_to_end(key) # Gotta keep this pair fresh, move to end of OrderedDict
            #self.dict[key] = value
        else: 
            if len(self.dict) >= self.capacity:
                self.dict.popitem(last=False)
            self.dict[key] = value 
