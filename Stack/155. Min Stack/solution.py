class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)

        #compare the min val then push in the min stack
        #compare if the minStack is not empty. If the minStack is empty, just push the origin val
        val = min(val, self.minStack[-1] if self.minStack else val) 
        self.minStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]