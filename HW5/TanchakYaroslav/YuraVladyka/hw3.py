number_facorial = int(input("Enter facorial:"))

factorial = 1
while number_facorial > 1:
    factorial *= number_facorial
    number_facorial -= 1

print(factorial)
