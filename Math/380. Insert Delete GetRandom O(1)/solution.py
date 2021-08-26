class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valDict = {}
        self.valList = []
        self.idx = 0
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.valDict:
            return False
        else:
            self.valDict[val] = self.idx
            self.valList.append(val)
            self.idx += 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.valDict:
            return False
        else:
            #find the old tail in the list 
            oldTail = self.valList[-1]
            
            # find the idx of the val that we want to remove
            i = self.valDict[val]

            # swap the val with the last element in the list
            self.valList[i], self.valList[-1] = self.valList[-1], self.valList[i]

            #update the idx of last element in the dict
            self.valDict[oldTail] = i

            #remove the val from the list and the dict
            self.valList.pop() 
            del self.valDict[val]

            #decrement idx
            self.idx -= 1

            return True
            


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.valList[floor(random.random()* self.idx)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()