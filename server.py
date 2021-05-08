from flask import Flask, render_template, url_for, request 
portfo = Flask(__name__)

@portfo.route('/')
def homePages():
    return render_template("index.html")

@portfo.route('/<page>')
def otherPage(page):
    return render_template(f"{page}.html")

@portfo.route("/submit_data" , methods = ["POST", "GET"])
def form_submition():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return "boooh yahhhh !!!!!"
    else:
        return "something went wrong________"