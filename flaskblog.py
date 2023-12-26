from flask import Flask, render_template, url_for, flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '96e16dc2e16030d974ef169fea42eec1'

posts = [
    {
        'author': 'Anh Tuan',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Thu hang',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 3, 2018'
    },
    {
        'author': 'Anh Khoa',
        'title': 'Blog post 3',
        'content': 'Third post content',
        'date_posted': 'April 12, 2018'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title ='About')


@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@blog.com' and form.password.data=='123456':
            flash(f'You have been login!','success')
            return redirect(url_for('home'))
        else:
            flash(f'login unsuccess, please check username and password','danger')
    return render_template('login.html',title='Login',form=form)

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account create for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

if __name__ == '__main__':
    app.run(debug=True)
    