class Employee():
    """
    A class that provides the number of employees and their names with salaries
    """
    employee_count = 0
    
    def __init__ (self,name,salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    def information(self):
        return (f"Name {self.name},salary - {self.salary}")
    @classmethod
    def employee_counter_method (cls):
        return(f"Employee count = {cls.employee_count}")
    
employee_1 = Employee("Yura",10250)
employee_2 = Employee("Anton",9550)
employee_3 = Employee("Orest",7650)

print(employee_1.information())
print(employee_2.information())
print(employee_3.information())

print(Employee.employee_counter_method())

print("Base classes :",Employee.__base__)     
print("Class namespace:", Employee.__dict__)    
print("Class name:", Employee.__name__)         
print("Module name:", Employee.__module__)      
print("Documentation:", Employee.__doc__) 
