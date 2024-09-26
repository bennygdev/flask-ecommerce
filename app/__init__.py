from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = '123456789'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)

  # Initlaise routes
  from .views import views

  app.register_blueprint(views, url_prefix="/")

  # Initialise Database
  from .models import User, Product, Role, Order, OrderItem, Category, ProductCategory

  create_database(app)
  
  return app

def create_database(app):
  with app.app_context():
    if not path.exists('instance/' + DB_NAME):
      db.create_all()
      print('Created Database!')