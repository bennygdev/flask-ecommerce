from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def dashboard_view(): # not dashboard for now, name conflict or may need a better name
  return render_template("dashboard/dashboard.html", user=current_user)

@dashboard.route('/profile')
@login_required
def profile():
  return render_template("dashboard/profile.html", user=current_user)

@dashboard.route('/orders')
@login_required
def orders():
  return render_template("dashboard/orders.html", user=current_user)