# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 使用flask模块来重写bottle中的例子


from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend：%s " % thing
