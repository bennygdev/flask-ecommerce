from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional

class LoginForm(FlaskForm):
  emailUsername = StringField('Email/Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
  submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
  firstName = StringField('First Name', validators=[DataRequired()])
  lastName = StringField('Last Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
  confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match")])
  username = StringField('Username', validators=[DataRequired()])
  submit = SubmitField('Submit')

class VariantForm(FlaskForm):
  title = StringField('Variant Title', validators=[DataRequired()])
  price = IntegerField('Price', validators=[DataRequired()])
  stock = IntegerField('Stock', validators=[DataRequired()])

class ProductForm(FlaskForm):
  name = StringField('Product Name', validators=[DataRequired(), Length(max=200)])
  description = TextAreaField('Description', validators=[Optional()])
  image_thumbnail = StringField('Image Thumbnail', validators=[Optional()])
  images = StringField('Images', validators=[Optional()])
  variants = FieldList(FormField(VariantForm), min_entries=1)  # 1 variant min
  category_id = IntegerField('Category ID', validators=[DataRequired()])
  submit = SubmitField('Add Product')