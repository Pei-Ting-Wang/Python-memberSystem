from flask import Flask
from flask import request
from flask import render_template

# static_folder=> 資料夾從public 跟目錄算 
app=Flask(__name__,static_folder="public",static_url_path='/')


@app.route("/")
def index():
    return "Hello World"

@app.route("/getName")
def getName():
    name=request.args.get("name","alex")
    return render_template("index.html",myname=name)  

app.run(port=3000)