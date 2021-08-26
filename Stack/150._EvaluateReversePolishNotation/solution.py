class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # the parameter order is important. For example, if we want to calculate "a - b", the "b" will be popped out before "a" is popped out.
        def eval(b , a , operator):
            if operator == "+":
                return a + b
            elif operator == "-":
                return a - b
            elif operator == "*":
                return a * b
            else:
                return int(a / b)
        
        stack = []
        op_check = {"+", "-","*","/"}

        for char in tokens:
            if char in op_check:
                stack.append(eval(stack.pop(), stack.pop(), char))
            else: 
                stack.append(int(char))
        return stack[-1]