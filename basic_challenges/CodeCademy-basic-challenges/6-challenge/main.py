def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return 'Enter a valid mathematical operator'


print('The program below is a simple calculator.')

first_number = float(input('Enter the first number: '))
operation = input('Select the mathematical operator: (+, -, /, or *): ')
second_number = float(input('Enter the second number: '))

result = calculator(first_number, second_number, operation)

print()
print(f'{first_number} {operation} {second_number} = {result}')
