from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Home page"

@app.route("/users")
def users():
    return "Welcome to users  page!"  

@app.route("/user/<name>")
def user(name):
    return f" Hello {name}"  

@app.route("/student/<name>/<course>")
def student(name,course):
    return f"  {name} is learing {course}"         

if __name__ == "__main__":
    app.run(debug=True) 