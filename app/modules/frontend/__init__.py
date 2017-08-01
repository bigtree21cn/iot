
from flask import render_template

def init_app(app):
    @app.route('/welcome1')
    def get():
        return render_template('welcome.html')