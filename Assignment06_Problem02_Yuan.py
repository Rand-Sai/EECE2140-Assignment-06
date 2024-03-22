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

