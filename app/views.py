from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
  return render_template("home.html")

@views.route('/products')
def products():
  return render_template("products.html")

@views.route('/saved')
def saved():
  return render_template("saved.html")

@views.route('/cart')
def cart():
  return render_template("cart.html")