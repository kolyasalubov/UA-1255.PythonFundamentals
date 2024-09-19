class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @staticmethod
    def print_total_employees():
        print(f"Загальна кількість працівників: {Employee.total_employees}")

    def employee_info(self):
        return f"Ім'я працівника: {self.name}, Зарплата: {self.salary}"

employee1 = Employee("Аліса", 50000)
employee2 = Employee("Богдан", 60000)

employee1.print_total_employees()
print(employee1.employee_info())
print(employee2.employee_info())

print(f"Базові класи: {Employee.__bases__}")
print(f"Простір імен класу: {Employee.__dict__}")
print(f"Назва класу: {Employee.__name__}")
print(f"Назва модуля: {Employee.__module__}")
print(f"Документація класу: {Employee.__doc__}")
