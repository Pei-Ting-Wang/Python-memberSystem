from unittest import result
from wsgiref.util import request_uri
from flask import Flask
from flask import request 
app=Flask(__name__) #建立 application 物件


#建立路徑 / getSum 對應的處理函式
#利用要求字串(Query String) 提供彈性:/getSum?max=100
@app.route("/getSum")
def getSum():
    maxNumber=request.args.get("max",100)
    maxNumber=int(maxNumber)
    result=0
    for n in range(1,maxNumber+1):
        result+=n
    return "結果"+str(result)



#建立路徑 / 對應的處理函式
@app.route('/')
def index():
    print("請求方法",request.method)
    print("通訊協定", request.scheme)
    print("主機名稱", request.host)
    print("路徑",request.path)
    print("完整的網址",request.url)
    print("瀏覽器和作業系統",request.headers.get('user-agent'))
    print("語言偏好",request.headers.get('accept-language'))
    print("引薦網址",request.headers.get('referrer'))
    return "Hello Flask" 
    
#建立路徑 / data的處理函式
# @app.route('/data')
# def handleData():
#     return "Handle Data"

# #動態路由
# @app.route('/user/<username>')
# def username(username):
#     return "Hello"+username

app.run(port=3000)
