from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '322209975e1d48ffa38481152ac73ed2'
if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:WJqlPyjvqOsaUjrQZpXWSmpXrFCwHrNl@postgres.railway.internal:5432/railway'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'É necessário estar logado para continuar'
login_manager.login_message_category = 'alert-info'

from forumdeduvidas import routes
