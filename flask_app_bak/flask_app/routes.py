from flask import Flask, render_template, request, redirect, url_for, flash, redirect
from flask_app import app
from flask_app.forms import RegistrationForm, LoginForm
from flask_app.models import User, Post

posts = [
  {
    'author': 'Saif Naqvi',
    'title': 'Blog post 1',
    'content': 'First post',
    'date_posted': 'February 23, 2021'
  },
  {
    'author': 'John Doe',
    'title': 'Blog post 2',
    'content': 'Second post',
    'date_posted': 'February 24, 2021'
  }
]


@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', posts=posts)


@app.route('/about')
def about():
  return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
      flash('Account created !', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login Unsuccessfull, Please check username and password', 'danger')
  return render_template('login.html', title='Login', form=form)