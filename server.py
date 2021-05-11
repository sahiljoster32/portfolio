from flask import Flask, render_template, url_for, request
import csv
import password as ps
import requests
import art_sticker as provider


portfo = Flask(__name__)

@portfo.route('/')
def homePages():
    return render_template("index.html")

@portfo.route("/specter" , methods = ["POST", "GET"])
def specter_shower():
    return render_template("specter.html", password_string = "Enter your password's value.", value = True)

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

@portfo.route("/value_pass", methods = ["POST", "GET"])
def password_provider():
    data1 = request.args.to_dict()
    with open("password_collection_data.csv", "a") as password_data:
        pass_value_writer = csv.DictWriter(password_data, fieldnames = ["name", "password"])
        pass_value_writer.writerow(data1)
    pass_password = data1["password"]
    flag = True
    count = ps.pass_main(pass_password)
    if count == 0:
        flag = False
    return render_template("specter.html", password_string = f"Password {pass_password} is appeared in {count} hacks", count_pass = flag)

@portfo.route("/phantom", methods= ["POST","GET"])
def random_image_provider():
    queries_data = request.args.to_dict()
    provider.imageProvider(queries_data["userstring"], queries_data["category"])
    return render_template("index.html")