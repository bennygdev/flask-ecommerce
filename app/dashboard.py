from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from .decorators import role_required
from . import db
from .models import Product
from .forms import ProductForm, VariantForm
import json

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
  product_list = Product.query.all()
  return render_template("dashboard/manage_products.html", products=product_list, user=current_user)

@dashboard.route('/add-product', methods=['GET', 'POST'])
@login_required
@role_required(2, 3)
def add_product():
  print('fail')
  form = ProductForm()
    
  if form.validate_on_submit():
    print('success')
    variants_data = [
      {
        "title": variant.title.data,
        "price": variant.price.data,
        "stock": variant.stock.data
      }
      for variant in form.variants.entries
    ]

    new_product = Product(
      name=form.name.data,
      description=form.description.data,
      image_thumbnail=form.image_thumbnail.data or None,
      images=form.images.data or None,
      category_id=form.category_id.data,
      variants=json.dumps(variants_data) # store as json
    )
        
    print('success')
    db.session.add(new_product)
    db.session.commit()
    # flash('Product added successfully!', 'success')
    return redirect(url_for('dashboard.manage_products'))
    # return redirect(url_for('dashboard.add_product'))

  # custom debugger
  if form.errors:
    print('Form failed to validate')
    for fieldName, errorMessages in form.errors.items():
      print(f"Error in {fieldName}: {errorMessages}")
    
  return render_template("dashboard/add_product.html", user=current_user, form=form)

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