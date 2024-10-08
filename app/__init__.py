from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from werkzeug.security import generate_password_hash
from flask_login import LoginManager, current_user
from flask_wtf.csrf import CSRFProtect
import json

db = SQLAlchemy()
DB_NAME = "database.db"
csrf = CSRFProtect()

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = '123456789'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)
  csrf.init_app(app)

  # Initlaise routes
  from .views import views
  from .auth import auth
  from .dashboard import dashboard

  app.register_blueprint(views, url_prefix="/")
  app.register_blueprint(auth, url_prefix="/")
  app.register_blueprint(dashboard, url_prefix="/")

  # Initialise Database
  from .models import User, Product, Role, Order, OrderItem, Category, ProductCategory

  create_database(app)

  # User load
  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))
  
  # 404, 403, 401 handler
  @app.errorhandler(404)
  def page_not_found(e):
    return render_template('404.html', user=current_user), 404
  
  @app.errorhandler(403)
  def forbidden(e):
    return render_template('403.html', user=current_user), 403

  @app.errorhandler(401)
  def unauthorized(e):
    return render_template('401.html', user=current_user), 401
  
  # json filter for displaying list of products
  @app.template_filter()
  def fromjson(value):
    return json.loads(value) if value else None

  return app

def create_database(app):
  with app.app_context():
    if not path.exists('instance/' + DB_NAME):
      db.create_all()
      print('Created Database!')
      insert_default_roles()
      insert_users()
      insert_categories()

def insert_default_roles():
  from .models import Role
  roles = ['Customer', 'Admin', 'Owner']

  for role_name in roles:
    role_exists = Role.query.filter_by(role_name=role_name).first()
    if not role_exists:
      new_role = Role(role_name=role_name)
      db.session.add(new_role)
    
  db.session.commit()
  print('Inserted default roles into the database!')

# insert admin and owner accounts here
def insert_users():
  from .models import User
  admin1 = User(
    first_name = "Admin", 
    last_name = "1",
    username = "admin1",
    email = "admin1@gmail.com",
    password = generate_password_hash("admin1", method='pbkdf2:sha256'),
    role_id = 2
  )

  admin2 = User(
    first_name = "Admin", 
    last_name = "2",
    username = "admin2",
    email = "admin2@gmail.com",
    password = generate_password_hash("admin2", method='pbkdf2:sha256'),
    role_id = 2
  )

  owner = User(
    first_name = "Owner", 
    last_name = "3",
    username = "owner",
    email = "owner@gmail.com",
    password = generate_password_hash("ownerApp", method='pbkdf2:sha256'),
    role_id = 3
  )

  users = [
    ("admin1@gmail.com", admin1),
    ("admin2@gmail.com", admin2),
    ("owner@gmail.com", owner)
  ]

  for email, user in users:
    existing_user = User.query.filter_by(email=email).first()
    if not existing_user:
      db.session.add(user)

  db.session.commit()
  print('Inserted Admin and Owner accounts!')

# insert product categories
def insert_categories():
  from .models import Category
  categories = ['Guitar & Basses', 'Keyboards & Pianos', 'Drums & Percussion', 'Vocals & Microphones', 'Vinyl & Cassettes']

  for category_name in categories:
    category_exists = Category.query.filter_by(category_name=category_name).first()
    if not category_exists:
      new_category = Category(category_name=category_name)
      db.session.add(new_category)
    
  db.session.commit()
  print('Inserted product categories into the database!')