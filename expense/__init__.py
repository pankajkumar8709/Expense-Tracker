from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///expense.db'
app.secret_key='8709'
db=SQLAlchemy(app)

from expense import routes