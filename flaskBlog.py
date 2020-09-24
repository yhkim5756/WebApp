from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '2727aba615ed000b4a9085e803b879d0'

posts = [
  {
    'author': 'Corey Schafer',
    'title': 'Blog Post 1',
    'content': 'first post content',
    'date_posted': 'April 20, 2018'
  },
  {
    'author': 'Jane Doe',
    'title': 'Blog Post 2',
    'content': 'second post content',
    'date_posted': 'May 01, 2018'
  }
]

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html', posts = posts)

@app.route("/about")
def about():
  return render_template('about.html', title = "About")

@app.route("/register", methods = ['GET', 'POST'])
def register():
  form = RegisterationForm()
  if form.validate_on_submit():
    flash(f'Account Created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title = 'Register', form=form)

@app.route("/login")
def login():
  form = LoginForm()
  return render_template('login.html', title = 'Login', form=form)