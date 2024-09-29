from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .decorators import role_required

dashboard = Blueprint('dashboard', __name__)

# @role_required() 1 = customer, 2 = admin, 3 = owner
# makes sure user roles can access a specific page

# changed from dashboard to overview
@dashboard.route('/overview')
@login_required
@role_required(1, 2, 3)
def overview():
  return render_template("dashboard/overview.html", user=current_user)

@dashboard.route('/profile')
@login_required
@role_required(1, 2, 3)
def profile():
  return render_template("dashboard/profile.html", user=current_user)

@dashboard.route('/orders')
@login_required
@role_required(1, 2, 3)
def orders():
  return render_template("dashboard/orders.html", user=current_user)

@dashboard.route('/manage-products')
@login_required
@role_required(2, 3)
def manage_products():
  return render_template("dashboard/manage_products.html", user=current_user)

@dashboard.route('/manage-accounts')
@login_required
@role_required(2, 3)
def manage_accounts():
  return render_template("dashboard/manage_accounts.html", user=current_user)

@dashboard.route('/add-account')
@login_required
@role_required(3)
def add_account():
  return render_template("dashboard/add_accounts.html", user=current_user)