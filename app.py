from flask import Flask, render_template,request,redirect,url_for,flash
#from uuid import UUID
import os


app = Flask(__name__)

app.secret_key="Production_of_proc"

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER,exist_ok=True)

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

@app.errorhandler(404)
def page_not_found(error):
     return render_template("404.html"),404     

@app.errorhandler(500)
def internal_server_error(error):
     return render_template("500.html"),500 

# @app.route("/test")
# def test():
#      # result 10/0   
#      return str(result)  

@app.route("/upload", methods=["GET","POST"])
def upload():
     if request.method == "POST":
          file= request.files.get("file")
          if not file:
               return  "Please select a file !"
          if file.filename == "":
               return "Please select a file"
          file.save(
                os.path.join(UPLOAD_FOLDER,file.filename)
          ) 
          return "File Uploaded Successfully"

     return render_template("upload.html")         
# @app.route("/search")
# def search():
#      query= request.args.get("query")
#      return f" you searched for: {query}"

if __name__ == "__main__":
    app.run(debug=True) 