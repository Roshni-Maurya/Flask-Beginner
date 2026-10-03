from flask import Flask, request
#from uuid import UUID

app = Flask(__name__)

@app.route("/search")  #query parameter
def search():
    name= request.args.get("name","Guest")  #defualt value
    course = request.args.get("course", "Unknown")
    return f"{name} is learning {course}"


if __name__ == "__main__":
    app.run(debug=True) 