class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeMatchOpen = {")": "(", "}": "{", "]": "["}

        for char in s:
            #if the char is a closing parenthese
            if char in closeMatchOpen:
                #the stack can not be empty and the most recent parenthese in stack should match char
                if stack and stack[-1] == closeMatchOpen[char]:
                    # if true, remove the stack[-1]
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        #return true only if the stack is empty after the loop
        return True if not stack else False