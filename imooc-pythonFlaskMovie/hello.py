#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description: 第一个Flask程序编写

from flask import Flask
app = Flask(__name__);

@app.route("/")
def index():
    return "<h1 style='color: red;'>这是一个简单的Flask程序</h1>";

if __name__  == "__main__":
    app.run();