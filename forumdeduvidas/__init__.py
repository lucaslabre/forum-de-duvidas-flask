from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

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

from forumdeduvidas import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table('usuario'):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print('Base de dados criada com sucesso!')
else:
    print('Base de dados já existente!')

from forumdeduvidas import routes
