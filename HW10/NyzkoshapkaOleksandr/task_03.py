class Employee ():
    
    amount_of_employees = 0
    
    def __init__(self, employee_name, employee_salary):
        self.employee_name = employee_name
        self.employee_salary = employee_salary
        Employee.amount_of_employees += 1
    @classmethod
    def count_of_employee(cls):
        return cls.amount_of_employees

    def show_amount_of_employees(self):
        print(f"Amount of employees: {Employee.count_of_employee()}")

    def get_information_about_employee(self):
        print (f"Name of employee: {self.employee_name} \nSalary: {self.employee_salary}")
        


employee_1 = Employee("Oleh", 9000)
employee_2 = Employee("Sasha", 15000)
employee_3 = Employee("Viktor", 10000)

employee_1.show_amount_of_employees()
employee_1.count_of_employee()
employee_1.get_information_about_employee()