#1.How do you create a basic Flask application
from flask import Flask
import warnings
warnings.filterwarnings("ignore")
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)


#2.How do you serve static files like images or CSS in Flask
    #Place them in a folder called static/
    #Access with: url_for('static', filename='style.css')
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<img src="{{ url_for('static', filename='logo.png') }}" />


#3.How do you define different routes with different HTTP methods in Flask
from flask import Flask, request  
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return "Form Submitted"
    return "Form Page"


#4.How do you render HTML templates in Flask
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


#5.How can you generate URLs for routes in Flask using url_for 
from flask import Flask, redirect, url_for
@app.route('/about')
def about():
    return "About Page"

@app.route('/')
def home():
    return redirect(url_for('about'))


#6.How do you handle forms in Flask 
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return f"Welcome, {username}"
    return render_template('login.html')


#7.How can you validate form data in Flask 
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            return '''
                <p style="color:red;">Name is required!</p>
                <form method="post">
                    <input type="text" name="name" placeholder="Enter your name">
                    <input type="submit" value="Submit">
                </form>
            '''
        return f'<h1>Hello, {name}!</h1>'
    
    return '''
        <form method="post">
            <input type="text" name="name" placeholder="Enter your name">
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)



#8.How do you manage sessions in Flask 
from flask import session

app.secret_key = 'your_secret_key'

@app.route('/set/')
def set_session():
    session['username'] = 'Amit'
    return "Session set"

@app.route('/get/')
def get_session():
    return session.get('username', 'Not set')


#9.How do you redirect to a different route in Flask 
from flask import Flask, redirect, url_for

@app.route('/old')
def old():
    return redirect(url_for('new'))

@app.route('/new')
def new():
    return "New Page"


#10.How do you handle errors in Flask (e.g., 404) 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


#11.How do you structure a Flask app using Blueprints 
  #my_blueprint/routes.py
from flask import Blueprint, render_template

# Create the Blueprint object
my_bp = Blueprint('my_bp', __name__)

# Define a route within the blueprint
@my_bp.route('/hello')
def hello():
    return render_template('hello.html', name="Amit")

   #in app.py
from flask import Flask
from my_blueprint import my_bp

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(my_bp, url_prefix='/bp')

if __name__ == '__main__':
    app.run(debug=True)



#12.How do you define a custom Jinja filter in Flask 
@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]
# In template: {{ "Flask" | reverse }} -> "ksalF"


#13.How can you redirect with query parameters in Flask 
@app.route('/search')
def search():
    query = request.args.get('q')
    return f"Search results for: {query}"

@app.route('/go')
def go():
    return redirect(url_for('search', q='Flask'))


#14.How do you return JSON responses in Flask 
from flask import jsonify

@app.route('/api/data')
def get_data():
    return jsonify({'name': 'Amit', 'age': 25})


#15.How do you capture URL parameters in Flask?
@app.route('/user/<username>')
def user_profile(username):
    return f"Hello, {username}"

@app.route('/post/<int:post_id>')
def post(post_id):
    return f"Post ID: {post_id}"
