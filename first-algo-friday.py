def perfect_square_checker(number):
    for potential_square in range(0, number+1):
        if potential_square * potential_square == number:
            return True 
    return False

def number_of_perfect_squares():
    start = int(input('Please enter a starting integer: '))
    end = int(input('Please enter an ending integer: '))
    perfect_square_count = 0

    for number in range(start, end):
        if(perfect_square_checker(number)):
            perfect_square_count = perfect_square_count + 1
    return perfect_square_count
print(number_of_perfect_squares())

def raise_number_to_power():
    number = int(input("Please enter a number: "))
    power = int(input("Please enter a power to raise it to: "))
    
    return print(f'The {number} raised by {power} is {number**power}')

raise_number_to_power()

