def perfect_square_checker(number):
    for potential_square in range(0, number+1):
        if potential_square * potential_square == number:
            return True 
    return False

def number_of_perfect_squares():
    start = int(input('Please enter a starting integer: '))
    end = int(input('Please enter an ending integer: '))
    perfect_square_count = 0

    for number in range(start, end+1):
        if(perfect_square_checker(number)):
            perfect_square_count = perfect_square_count + 1
    return perfect_square_count
print(number_of_perfect_squares())