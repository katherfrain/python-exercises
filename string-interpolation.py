def add(number1, number2):
    return number1 + number2

def calculator():
    first_number = float(input('Please enter first number: '))
    operand = input('What is the operand? ')
    second_number = float(input('Please enter the second number: '))

    print(f'You want to see the equation {first_number} {operand} {second_number}')

    if operand == '+':
        print(add(first_number, second_number))


calculator()


