from flask import Flask,request
from main import run_all
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def i():
    if request.method=="POST":
        return str(run_all(request.form["code"]))
    return '<form method=post><textarea name=code></textarea><button>Run</button></form>'

app.run()
