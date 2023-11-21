from flask import Flask,render_template, request
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def index():
    X="江朝安求職自傳履歷網頁<br>"
    X+="<a href=/about>關於江朝安</a><br>"
    X+="<a href=/Holla>何倫碼</a><br>"
    X+="<a href=/imgwork>相關工作介紹</a><br>"
    X+="<a href=/selfex>未來目標</a><br>"
    return X

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/Holla")
def Holla():
    return render_template("Holla.html")
@app.route("/imgwork")
def imgwork():
    return render_template("imgwork.html")   
@app.route("/selfex")
def selfex():
    return render_template("selfex.html")

if __name__ == "__main__":

	app.run(debug=True)