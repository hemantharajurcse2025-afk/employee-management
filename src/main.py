from employee import Employee


employees = []


def add_employee():
    employee_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    employee = Employee(
        employee_id,
        name,
        email,
        department,
        salary
    )

    employees.append(employee)
    print("Employee added successfully.")


def view_employees():
    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        employee.display()


def search_employee():
    employee_id = input("Enter Employee ID to search: ")

    for employee in employees:
        if employee.employee_id == employee_id:
            employee.display()
            return

    print("Employee not found.")


def delete_employee():
    employee_id = input("Enter Employee ID to delete: ")

    for employee in employees:
        if employee.employee_id == employee_id:
            employees.remove(employee)
            print("Employee deleted successfully.")
            return

    print("Employee not found.")


def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()