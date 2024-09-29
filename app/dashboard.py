from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard = Blueprint('dashboard', __name__)

# changed from dashboard to overview
@dashboard.route('/overview')
@login_required
def overview():
  return render_template("dashboard/overview.html", user=current_user)

@dashboard.route('/profile')
@login_required
def profile():
  return render_template("dashboard/profile.html", user=current_user)

@dashboard.route('/orders')
@login_required
def orders():
  return render_template("dashboard/orders.html", user=current_user)

# Please make sure to restrict access to customers for this page

# Please make sure to restrict access to customers and admins for this page