from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fake data (temporary)
students = [
    {"id": 1, "name": "Alice", "points": 10, "avatar": "😀"},
    {"id": 2, "name": "Bob", "points": 8, "avatar": "🐱"},
    {"id": 3, "name": "Charlie", "points": 5, "avatar": "🐻"},
]

# Home -> redirect to class view
@app.route("/")
def home():
    return redirect(url_for("view_class", class_id=1))

# Fake class page
@app.route("/class/<int:class_id>")
def view_class(class_id):
    return render_template("students.html", students=students)

# Award points (in memory)
@app.route("/award/<int:student_id>", methods=["POST"])
def award_points(student_id):
    for student in students:
        if student["id"] == student_id:
            student["points"] += 1
    return redirect(url_for("view_class", class_id=1))

@app.route("/classroom")
def classroom():
    return render_template("classroom.html")

if __name__ == "__main__":
    app.run(debug=True)

