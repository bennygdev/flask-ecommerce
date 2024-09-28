from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
  return render_template("login.html")

@auth.route('/logout')
# @login_required
def logout():
  return "Log out"

@auth.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    email = request.form.get('email')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')
    username = request.form.get('username')

    # print(request.form)
    # server side validation
    if (not firstName or len(firstName) < 1 or not lastName or len(lastName) < 1 or
        not email or len(email) < 1 or not password or len(password) < 6 or 
        password != confirmPassword or not username or len(username) < 1):
      print('invalid')
      return
    else:
      # auth side not added yet
      return redirect(url_for('views.home')) 
    
  return render_template("register.html")

