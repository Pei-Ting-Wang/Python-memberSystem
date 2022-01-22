from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__,static_folder="public", static_url_path='/')

#使用post方法
@app.route('/')
def index():
    return render_template('form.html')

@app.route('/show',methods=["POST"])
def show():  
    # name=request.args.get('n')
    name=request.form['n']
    return "Hello"+name
app.run(port=3000)
