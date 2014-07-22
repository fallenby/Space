from flask import Flask
from flask import render_template

from jinja2 import Environment, PackageLoader

class Flask(Flask):
    jinja_options = dict(trim_blocks = True, lstrip_blocks = True)

app = Flask(__name__)

# Default script files
scripts = ['anus.js']

# Default stylesheets
styles = ['anus.css']

# Default meta tags
metas = [{"description" : "Space, the Timesheet management system"}]

@app.route('/')
def index():
    return render_template('site/base/base_basic.html', scripts=scripts, metas=metas, styles=styles)

@app.route('/login')
def login():
    return render_template('site/login/login.html')

if __name__ == '__main__':
    app.run(debug=True)


