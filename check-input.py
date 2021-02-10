
class Calculator:
    def __init__(self, first_number, second_number, operand):
        self.first_number = first_number
        self.second_number = second_number
        self.operand = operand

    def add(self):
        return self.first_number + self.second_number

    def subtract(self):
        return self.first_number - self.second_number

    def check_operand(self):
        if self.operand == '+':
            print('We are definitely doing addition here')
            print(self.add())
        elif self.operand == '-':
            print('This is a subtraction!!!')
            print(self.subtract())
    

calc = Calculator(1, 3, '+')
calc.check_operand()