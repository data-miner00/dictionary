from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

from app import routes

# Register blueprint(s)
# app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)

# db.create_all()
