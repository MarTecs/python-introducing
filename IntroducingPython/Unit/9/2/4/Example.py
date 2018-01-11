# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 使用一个轻量级的Python Web框架

from bottle import route, run

@route('/')
def home():
    return "It isn't fancy, but it's my home page"

run(host='localhost', port=9999)