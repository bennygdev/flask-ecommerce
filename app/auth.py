from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import User
from .forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    emailUsername = form.emailUsername.data
    password = form.password.data
        
    user = User.query.filter((User.email == emailUsername) | (User.username == emailUsername)).first()

    if user and check_password_hash(user.password, password):
      login_user(user, remember=True)
      return redirect(url_for('views.home'))
    else:
      form.password.errors.append('Invalid email or password')

  return render_template("auth/login.html", user=current_user, form=form)

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  print("Logged out user")
  return redirect(url_for('auth.login')) # switch to home

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

    # server side validation kinda needed for duplicate email + username
    user_exists = User.query.filter_by(email=email).first()
    email_exists = User.query.filter_by(username=username).first()

    if (user_exists or email_exists):
      # validation needed...
      print('Username or email already exists')
      return 'None'
    elif (not username or len(username) < 1 or not firstName or len(firstName) < 1 or not lastName or len(lastName) < 1 or not email or len(email) < 1 or len(password) < 6 or len(confirmPassword) < 6):
      print('invalid')
      return 'Invalid validation'
    else:
      # add user to database
      new_user = User(
        first_name = firstName, 
        last_name = lastName,
        username = username,
        email = email,
        password = generate_password_hash(password, method='pbkdf2:sha256'),
        role_id = 1
      )
      db.session.add(new_user)
      db.session.commit()
      print('account created successfully')
      return redirect(url_for('views.home')) # redirect the user to login?
    
  return render_template("auth/register.html", user=current_user)

