from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Here i wrote database setup and configuration
from app import database


# Here i wrote all the View logics and functions
from app import routes