def evaluate_expression(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char in operators:
            op2 = stack.pop()
            op1 = stack.pop()
            if char == '+':
                stack.append(op1 + op2)
            elif char == '-':
                stack.append(op1 - op2)
            elif char == '*':
                stack.append(op1 * op2)
            elif char == '/':
                stack.append(op1 / op2)

    return stack[0]

# Test the function
expression = "23+5*2"
print("Expression:", expression)
print("Result:", evaluate_expression(expression))