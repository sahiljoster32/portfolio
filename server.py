from flask import Flask, render_template, url_for, request
import csv
import password as ps
import art_sticker as provider
import string 
import random

portfo = Flask(__name__)

@portfo.route('/')
def homePages():
    
    S = 20
    
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    random_string = str(ran) 
    
    return render_template("index.html", source_icon = f"https://robohash.org/{random_string}?set=set4")

@portfo.route("/specter" , methods = ["POST", "GET"])
def specter_shower():
    
    S = 20
    
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    random_string = str(ran) 
    
    return render_template("specter.html", password_string = "Enter your password's value.", value = True, source_icon = f"https://robohash.org/{random_string}?set=set4")

@portfo.route('/<page>')
def otherPage(page):
    
    S = 20
    
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    random_string = str(ran)
    
    if page == "index":
        set_value = "set4"
    if page == "works":
        set_value = "set1"
    if page == "about":
        set_value = "set3"
    if page == "contact":
        set_value = "set2" 
    elif page not in ["index", "works","about","contact"]:
        set_value = "set3"   

    return render_template(f"{page}.html", source_icon = f"https://robohash.org/{random_string}?set={set_value}")          

@portfo.route("/submit_data" , methods = ["POST", "GET"])
def form_submition():
    
    if request.method == "POST":
        data = request.form.to_dict()
    
        with open("./records/data_form.csv" , "a") as data_form:
            data_writer = csv.DictWriter(data_form, fieldnames = ["email", "subject", "message"])
            data_writer.writerow(data)
    
            return render_template("thank.html")
    
    else:
        return "something went wrong - please try some time after."

@portfo.route("/value_pass", methods = ["POST", "GET"])
def password_provider():
    
    data1 = request.args.to_dict()
    
    with open("./records/password_collection_data.csv", "a") as password_data:
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
    
    source_image =  provider.imageProvider(queries_data["userstring"], queries_data["category"])
    
    return render_template("operator.html" , userstring = queries_data["userstring"], category = queries_data["category"], source_image =source_image)