class Solution:
    def evalRPN(self, tokens):
        stack = []  # Stack to store numbers
        
        for token in tokens:
            if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
                # If the token is an operand, push it onto the stack
                stack.append(int(token))
            else:
                # If the token is an operator, pop required operands and perform the operation
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == "+":
                    stack.append(operand1 + operand2)
                elif token == "-":
                    stack.append(operand1 - operand2)
                elif token == "*":
                    stack.append(operand1 * operand2)
                elif token == "/":
                    stack.append(int(operand1 / operand2))
        
        return stack[0]  # Return the final result
