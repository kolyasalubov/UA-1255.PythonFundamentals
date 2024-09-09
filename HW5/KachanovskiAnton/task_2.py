fibonacci_sequence_list = [0, 1]
maximum_number_of_fibonacci_sequence = int(input("Enter a maximum number of Fibonacci sequence: "))

first_number, second_number = 0, 1

while True:
    first_number, second_number = second_number, first_number + second_number
    if first_number > maximum_number_of_fibonacci_sequence:
        break
    fibonacci_sequence_list.append(first_number)

print(f"Fibonacci sequence up to {maximum_number_of_fibonacci_sequence}: {fibonacci_sequence_list}")