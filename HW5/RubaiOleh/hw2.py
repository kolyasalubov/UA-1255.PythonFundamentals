def fibonacci(n):
  fib_list = [0, 1]
  while fib_list[-1] < n:
    next_fib = fib_list[-1] + fib_list[-2]
    fib_list.append(next_fib)
  return fib_list

# Отримання числа n від користувача
n = int(input("Введіть число n: "))

# Обчислення і виведення чисел Фібоначчі
result = fibonacci(n)
print(result)