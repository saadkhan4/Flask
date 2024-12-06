from flask import Flask, redirect , render_template ,request, session 
from flask_session import Session 


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False   # as soon as you quit the browser your session will be deleted.
app.config["SESSION_TYPE"] = "filesystem" # contents of your shopping cart stores in servers.
Session(app)

@app.route("/")
def index():
   return render_template("index.html", name=session.get("name"))


@app.route("/login" , methods=["GET" , "POST"])
def login():
   if request.method == "POST":
      session["name"] = request.form.get("name")
      return redirect("/") 
   return render_template("login.html")