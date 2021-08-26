class Solution:
    def decodeString(self, s: str) -> str:
        stack = [["", 1]] #the initial array in stack is for storing the result string

        num = 0       

        for char in s:
            if char.isdigit():
                num = num*10 + int(char) # this helps us to keep track of more than 1 digit number
            elif char == "[":
                stack.append(["", num])
                num = 0
            elif char == "]":
                string, k = stack.pop()
                stack[-1][0] += string * k
            else:
                stack[-1][0] += char

        return stack[-1][0]

