from flask import *
import pymongo
app=Flask(
    __name__,
    static_folder='public',
    static_url_path='/')

client = pymongo.MongoClient("mongodb+srv://root:root123@mycluster.yufcy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.memberSystem

#首頁
@app.route('/')
def index():
    return render_template("index.html")

#會員頁面
@app.route('/member')
def member():
    if("nickname" in session):
        return render_template("member.html")
    return redirect("/")
#註冊
@app.route('/signup',methods=["POST"])
def signup():
    nickname=request.form["nickname"]
    email=request.form["email"]
    password=request.form["password"]
    #根據接收到的資料跟資料庫互動
    collection=db.user
    result=collection.find_one({
        "email":email
    })
    if result !=None:
        return redirect("/error?msg=信箱已被註冊")
    collection.insert_one({
        "nickname":nickname,
        "email":email,
        "password":password
    })
    return redirect("/")

#登入
@app.route('/signin',methods=["POST"])
def signin():
    email=request.form["email"]
    password=request.form["password"]
    collection=db.user
    result=collection.find_one({
        "$and":[
            {"email":email},
            {"password":password}
        ]
    })
    if result == None:
        return redirect("/error?msg=帳號密碼錯誤")
    session["nickname"]=result["nickname"]
    return redirect('/member')

#登出
@app.route("/signout")
def signout():
    del session["nickname"]
    return redirect('/')

#錯誤頁面
@app.route('/error')
def error():
    msg=request.args.get("msg","發生錯誤!!")
    return render_template("error.html",msg=msg)
    
app.secret_key="any string but secret"
app.run(port=3000)