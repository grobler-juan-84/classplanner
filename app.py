from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# -------------------
# Flask App Setup
# -------------------
app = Flask(__name__)

# Configure SQLite Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Database
db = SQLAlchemy(app)

# -------------------
# Database Models
# -------------------
class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    students = db.relationship("Student", backref="class_", lazy=True)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, default=0)
    class_id = db.Column(db.Integer, db.ForeignKey("class.id"), nullable=False)

# -------------------
# Routes
# -------------------
@app.route("/")
def home():
    return "<h1>Classroom Management Tool</h1><p>Database is ready!</p>"

# -------------------
# Create Database
# -------------------
with app.app_context():
    db.create_all()

# -------------------
# Run the App
# -------------------
if __name__ == "__main__":
    app.run(debug=True)

