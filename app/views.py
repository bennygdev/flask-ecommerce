from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
  return render_template("views/home.html", user=current_user)

@views.route('/products')
def products():
  return render_template("views/products.html", user=current_user)

@views.route('/saved')
def saved():
  return render_template("views/saved.html", user=current_user)

@views.route('/cart')
def cart():
  return render_template("views/cart.html", user=current_user)