from flask import Flask, render_template
#from uuid import UUID

app = Flask(__name__)

@app.route("/")
def home():
    courses = [
        "python",
        "dbs",
        "react",
        "java",
        "jija2"
    ]
    student = {
        "Name":"Roshni",
        "Class" :"3rd Year",
        "Subject":"Python"
    }
    return render_template("index.html", courses=courses,student=student)

if __name__ == "__main__":
    app.run(debug=True) 