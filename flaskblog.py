from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c73b73bf477f6dad17f96e12b9a5830f'

posts = [
    {
        'author': 'Francisco Ramirez',
        'date': '2021-11-01',
        'title': 'First blog post',
        'content': 'Blog post 1',
    },

    {
        'author': 'Francisco Ramirez',
        'date': '2021-11-02',
        'title': 'Second blog post',
        'content': 'Gotta push to git',
    }
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been log in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check username a password.', 'danger')
    return render_template('login.html', title='Login', form=form)
    

if __name__ == '__main__':
    app.run(debug=True)
