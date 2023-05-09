string = input("Enter the postfix expression: ")
stack = []

def calculate_result(string):
    characters = {'+': '+', '-': '-', '*': '*', '/': '/'}
    tokens = string.split()
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in characters:
            operando2 = stack.pop()
            operando1 = stack.pop()
            resultado = None
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                resultado = operando1 / operando2
            elif token == '%':
                resultado = operando1 % operando2
            elif token == '**':
                resultado = operando1 ** operando2
            stack.append(resultado)
    return stack.pop()

print("The result of: ", string, "is: ", calculate_result(string))
