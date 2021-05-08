from flask import Flask, render_template, url_for, request 
import csv
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
        with open("data_form.csv" , "a") as data_form:
            data_writer = csv.DictWriter(data_form, fieldnames = ["email", "subject", "message"])
            data_writer.writerow(data)
            return render_template("thank.html")
    else:
        return "something went wrong - please try some time after."