class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack, curr_num = [], 0

        # declare default operator as "+" is because we want to append the first number in the string into the stack
        operator = "+"

        #to check the char
        operator_check = {"+", "-", "*", "/"}
        nums = set(str(x) for x in range(10))

        for index in range(len(s)):
            char = s[index]

            #if we meet a number, we update the curr_num and wait until we meet the operator to process it into the stack
            if char in nums:
                curr_num = curr_num*10 + int(char)

            #if we meet a operator, we deal with the previous operator store in the operator variable and the curr_num.
            #Important if the char moves to the end of the string, we also need to deal with the previous operator.
            if char in operator_check or index == len(s) -1:
                if operator == "+":
                    stack.append(curr_num)
                elif operator == "-":
                    stack.append(-curr_num)
                elif operator == "*":
                    stack[-1] *= curr_num
                elif operator == "/":
                    stack[-1] = int(stack[-1] / curr_num)
                    # int() to truncate the division into interger
                
                #update the variable
                operator = char
                curr_num = 0

        #add up all stack elements    
        return sum(stack)