from flask import Flask, render_template,request,redirect,url_for,flash
#from uuid import UUID


app = Flask(__name__)

app.secret_key="Production_of_proc"

@app.route("/")
def home():
     return render_template("index.html")

@app.route("/about")
def about():
     return render_template("about.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
     if request.method == 'POST':
          username = request.form.get("username","").strip()
          email = request.form.get("email","").strip()
          age = request.form.get("age","").strip()
         
          if not username:
               flash("Name is required !","danger")
               return redirect(url_for("contact"))
          if not email:
               flash("Email is required !","danger")
               return redirect(url_for("contact")) 
          if not age:
               flash("Age is required !","danger")
               return redirect(url_for("contact"))
          if  not age.isdigit():
               return "Age must be a number"   
          flash("Registration Successull !","success")

     return render_template("contact.html")     
@app.route("/success")
def success():
     return "Registration Successfull"

# @app.route("/search")
# def search():
#      query= request.args.get("query")
#      return f" you searched for: {query}"

if __name__ == "__main__":
    app.run(debug=True) 