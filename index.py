from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    X = "作者：資管二Ａ 習祐翔 Danny <br>"
    X += "<a href=/aboutme>我的個人簡介</a><br>"
    X += "<a href=/account>MIS相關工作介紹</a><br>"
    X += "<a href=/today>職涯測驗結果</a><br>"
    X += "<a href=/welcome>未來規劃</a><br>"
    return X

@app.route("/today")
def today():
    return render_template("today.html")

@app.route("/aboutme")
def about():
    return render_template("aboutme.html")  

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/account")
def account():
    return render_template("account.html")

if __name__ == "__main__":
    app.run()