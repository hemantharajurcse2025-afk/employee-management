class Employee:
    def __init__(self, employee_id, name, email, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary

    def display(self):
        print(f"ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print("-" * 30)