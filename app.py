from flask import Flask, render_template
#from uuid import UUID

app = Flask(__name__)

@app.route("/")
def home():
    name="Roshni"  #dynamic name
    course ="Flask"
    city ="kalyan"
    age =24
    return render_template("index.html",name=name,
    course=course,
    city=city,age=age)

if __name__ == "__main__":
    app.run(debug=True) 