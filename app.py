from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database config - creates a file called classroom.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///classroom.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, default=0)
    avatar_url = db.Column(db.String(200), default="https://placekitten.com/200/200")

    # Foreign key to connect to Class
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)

    def __repr__(self):
        return f"<Student {self.name} - {self.points} pts>"

# Class model
class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # One-to-many relationship: a Class has many Students
    students = db.relationship('Student', backref='classroom', lazy=True)

    def __repr__(self):
        return f"<Class {self.name}>"



@app.route("/")
def index():
    # For now, just grab the first class
    class1 = Class.query.first()
    students = class1.students if class1 else []
    return render_template("index.html", students=students, classroom=class1)


if __name__ == "__main__":
    # Create the database file if it doesn't exist
    if not os.path.exists("classroom.db"):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
