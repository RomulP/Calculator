# a brilliant creation of a mad mind

a, operator, b = int(input()), input(), int(input())

if operator == '+':
	answer = a + b 
elif operator == '-':
	answer = a - b
elif operator == '*':
	answer = a * b
elif operator == '/':
	answer = a / b

print(f'{a} {operator} {b} = {answer}')