from flask import Flask, render_template, request, redirect, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '23df2424'

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
    flash('Account created !', 'success')
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


if __name__ == '__main__':
  app.run(debug=True)
