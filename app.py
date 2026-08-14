from flask import Flask, render_template, request, redirect
from src.employee import Employee

app = Flask(__name__)

employees = []


@app.route("/")
def home():
    return render_template(
        "index.html",
        employees=employees
    )


# ADD EMPLOYEE
@app.route("/add", methods=["POST"])
def add_employee():

    employee_id = request.form["employee_id"]
    name = request.form["name"]
    email = request.form["email"]
    department = request.form["department"]
    salary = request.form["salary"]

    employee = Employee(
        employee_id,
        name,
        email,
        department,
        salary
    )

    employees.append(employee)

    return redirect("/")


# EDIT EMPLOYEE
@app.route("/edit/<employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):

    employee = next(
        (emp for emp in employees if emp.employee_id == employee_id),
        None
    )

    if employee is None:
        return "Employee not found", 404

    if request.method == "POST":

        employee.name = request.form["name"]
        employee.email = request.form["email"]
        employee.department = request.form["department"]
        employee.salary = request.form["salary"]

        return redirect("/")

    return render_template(
        "edit.html",
        employee=employee
    )


# DELETE EMPLOYEE
@app.route("/delete/<employee_id>")
def delete_employee(employee_id):

    global employees

    employees = [
        emp for emp in employees
        if emp.employee_id != employee_id
    ]

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)