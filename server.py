from flask import Flask, render_template, url_for
portfo = Flask(__name__)

@portfo.route('/')
def homePages():
    return render_template("index.html")

@portfo.route('/<page>')
def otherPage(page):
    return render_template(f"{page}.html")

