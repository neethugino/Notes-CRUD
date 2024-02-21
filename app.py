# importing necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key_for_jwt'
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)