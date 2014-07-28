from app import Flask
from flask import render_template
from flask import url_for

from jinja2 import Environment, PackageLoader

app = Flask(__name__)
app.config.from_object('config.development.Config')

@app.route('/')
def index():
    return render_template('site/index/base.html')

@app.route('/login')
def login():
    return render_template('site/login/login.html')

if __name__ == '__main__':
    app.run(debug=True)


