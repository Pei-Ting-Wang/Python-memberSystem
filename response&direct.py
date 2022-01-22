from flask import Flask
from flask import request
from flask import redirect  
import json
app=Flask(__name__) #建立 application 物件


@app.route("/")
def index():
    lang=request.headers.get('accept-language')
    if(lang.startswith("en")):
        return json.dumps({
            "status":"ok",
            "text":"Hello World"
        })
    else:
        return json.dumps({
            "status":"ok",
            "text":"歡迎光臨"
        },ensure_ascii=False)
@app.route("/google")
def google():
    return redirect("https://google.com")
app.run(port=3000)
