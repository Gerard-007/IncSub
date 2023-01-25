from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_migrate import Migrate


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'

db = SQLAlchemy(app)
# migrate = Migrate(app, db)
migrate = Migrate(app, db, command='migrate')

# Import All Models
from . import models

# import serializers
from . import serializers

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()
