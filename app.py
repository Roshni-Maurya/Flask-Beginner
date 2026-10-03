from flask import Flask
from uuid import UUID
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Home page"

@app.route("/user/<int:id>")  #int converter
def user(id):
    return f" User ID:  {id}"

@app.route("/price/<float:amount>")  #float converter
def price(amount):
    return f" Product Price:  {amount}"   

@app.route("/files/<path:file_path>")  #path converter
def files(file_path):
    return file_path  

@app.route("/student/<uuid:user_id>")  #path converter
def student(user_id):
    return str(user_id)            

if __name__ == "__main__":
    app.run(debug=True) 