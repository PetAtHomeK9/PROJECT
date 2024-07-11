"""1. Write a Python class Employee with attributes like emp_id, emp_name,
 emp_salary, and emp_department and methods like calculate_emp_salary, 
 emp_assign_department, and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"

Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked,
 which is the number of hours worked by the employee.
   If the number of hours worked is more than 50,
     the method computes overtime and adds it to the salary. 
     Overtime is calculated as following formula:
overtime = hours_worked - 50

Overtime amount = (overtime * (salary / 50))"""


class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
        salary = 0 


    def calculate_emp_salary(self,salary, hours_worked ):
        self.salary = salary
        if hours_worked > 50:
            overtime = hours_worked - 50
            Overtime_amount = (overtime * (salary / 50))
            salary += overtime
            return salary
                               

    def emp_assign_department(self, New_Department):
        self.New_Department = New_Department

    def print_employee_details(self):
        print(f"{self.emp_name}, {self.emp_id}, {self.emp_salary}, {self.emp_department}")


ADAMS = Employee( "ADAMS", "E7876", 50000, "ACCOUNTING")
JONES = Employee("JONES", "E7499", 45000, "RESEARCH")
MARTIN = Employee("MARTIN", "E7900", 50000, "SALES")
SMITH = Employee("SMITH", "E7698", 55000, "OPERATIONS")