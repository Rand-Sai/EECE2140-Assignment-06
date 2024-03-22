#Assignment 06 - Problem Employee Management System

#Develop an employee management system where Employee is a base class with attributes like name and
#position, and methods such as calculate_salary(). Derive different classes such as HourlyEmployee,
#SalariedEmployee, and CommissionEmployee that each have different implementations of the
#calculate_salary() method. Implement a function that processes a list of employees and calculates their
#salary using polymorphism, without needing to check the type of each employee.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def calculate_salary(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, name, position, wage, hours):
        super().__init__(name, position)
        self.wage = wage
        self.hours = hours

    def calculate_salary(self):
        salary = self.wage * self.hours
        print('Your salary is: $' + str(salary))

class SalariedEmployee(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position)
        self.salary =salary

    def calculate_salary(self):
        print('Your annual salary is: $' + str(self.salary))

class CommissionEmployee(Employee):
    def __init__(self, name, position, commission_rate, total_sale):
        super().__init__(name, position)
        self.commission_rate = commission_rate
        self.total_sale = total_sale

    def calculate_salary(self):
        salary = self.commission_rate/100 * self.total_sale
        print('Your salary is: $' + str(salary))

#-----------------------------------------------------
def main():
    employees = [
        HourlyEmployee('Jack', 'PartTime', 25, 400),
        SalariedEmployee('Jason', 'Senior Designer', 60000),
        CommissionEmployee('Jaclyn', 'Sales', 12, 7000000)
        ]
    
    #iterate
    for employee in employees:
        employee.calculate_salary()

#----------------------------------------------------------
main()