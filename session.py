from flask import Flask
from flask import request
from flask import session 


app=Flask(__name__)
#設定Secret key 
app.secret_key="anyStringButSecret"

@app.route('/')
def hello():
    name=request.args.get("name","")
    session["username"]=name #session["欄位"]=資料
    return "你好"+name
@app.route('/talk')
def talk():
    name=session["username"]
    return name
app.run(port=3000)