from flask import Flask, render_template
#from uuid import UUID

app = Flask(__name__)

@app.route("/")
def home():
    first_name="Roshni"
    last_name="Maurya"  
    city ="kalyan"
    price =2400
    course =["python",
    "java",
    "django",
    "FastAPI"]
    return render_template("index.html",first_name=first_name,
    last_name=last_name,
    course=course,
    city=city,price=price)

if __name__ == "__main__":
    app.run(debug=True) 