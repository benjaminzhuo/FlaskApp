from flask import Flask, render_template
#Articles function from our data.py file
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form. StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/articles')
def articles():
	return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>')
def article(id):
	return render_template('article.html', id = id)

class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min = 1, max = 50)])
	usernane = StringField('Username', [validators.Length(min = 4, max = 25)])


if __name__ == '__main__':
	app.run(debug = True)
