from flask import Flask, render_template,request
#from uuid import UUID

app = Flask(__name__)

@app.route("/")
def home():
     return render_template("index.html")

@app.route("/about")
def about():
     return render_template("about.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
     if request.method == 'POST':
          name = request.form.get("username","").strip()
          email = request.form.get("email","").strip()
          message = request.form.get("age","").strip()
         
          if not username:
              return "Name is required" 
          if not email:
               return "Email is required" 
          if not age:
              return "Age is required"   
          if  age.isdigit():
               return "Age must be a number"   
     return "Registration Successfully Completed"

     return render_template("contact.html")     

# @app.route("/search")
# def search():
#      query= request.args.get("query")
#      return f" you searched for: {query}"

if __name__ == "__main__":
    app.run(debug=True) 