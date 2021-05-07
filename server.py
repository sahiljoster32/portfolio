from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(url_for('static', filename='bolt.ico'))
    return 'hihihi'

@app.route('/hello')
def newpage():
    return render_template("index.html")

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/jjj')
def index():
    
    return 'index'

@app.route('/login')
def login():
    return "login"

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))