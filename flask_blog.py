from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ab1f25d0a160b87ad310899a2fe88d34'

posts = [
    {'author': 'Fiona Glory',
     'title': 'Infinite Beginnings',
     'content': 'Peace, Love and Joy',
     'date_posted': 'June 2, 2000'
     }, {
        'author': 'Fiona Alulu',
        'title': 'Finite Endings',
        'content': 'Money, Love and Robots',
        'date_posted': 'July 8, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', category="success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have ben logged-in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful! Please Check Username and Password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
