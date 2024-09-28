from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
  return render_template("home.html", user=current_user)

@views.route('/products')
def products():
  return render_template("products.html", user=current_user)

@views.route('/saved')
def saved():
  return render_template("saved.html", user=current_user)

@views.route('/cart')
def cart():
  return render_template("cart.html", user=current_user)

@views.route('/dashboard')
@login_required
def dashboard():
  return render_template("dashboard.html", user=current_user)

@views.route('/profile')
@login_required
def profile():
  return render_template("profile.html", user=current_user)

@views.route('/orders')
@login_required
def orders():
  return render_template("orders.html", user=current_user)