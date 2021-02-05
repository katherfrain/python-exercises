def fibonacci():
    first_fibonacci_number = int(input('Please enter the first number to seed your Fibonacci sequence: '))
    second_fibonacci_number = int(input('Please enter the second number to seed your Fibonacci sequence: '))
    iterator_count = int(input("Please indicate the number of steps you want your Fibonacci sequence to perform: "))

    fibonacci_sequence = [first_fibonacci_number, second_fibonacci_number]
    current_fibonacci_number = 0

    for i in range(2, iterator_count):
        current_fibonacci_number = fibonacci_sequence[i - 2] + fibonacci_sequence[i -1]
        fibonacci_sequence.append(current_fibonacci_number)
    return fibonacci_sequence


print(fibonacci())