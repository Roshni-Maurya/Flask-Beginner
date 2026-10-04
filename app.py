from flask import Flask, render_template
#from uuid import UUID

app = Flask(__name__)

@app.route("/")
def home():
    is_logged_in = True
    return render_template("index.html", is_logged_in=is_logged_in)

if __name__ == "__main__":
    app.run(debug=True) 