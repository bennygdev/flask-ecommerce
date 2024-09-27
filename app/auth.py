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

@auth.route('/register')
def register():
  return render_template("register.html")

