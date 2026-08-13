from flask import Flask, render_template, request, redirect

app = Flask(__name__)

employees = []


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        employee_id = request.form["employee_id"]
        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        salary = request.form["salary"]

        employee = {
            "employee_id": employee_id,
            "name": name,
            "email": email,
            "department": department,
            "salary": salary
        }

        employees.append(employee)

        return redirect("/")

    return render_template(
        "index.html",
        employees=employees
    )


if __name__ == "__main__":
    app.run(debug=True)