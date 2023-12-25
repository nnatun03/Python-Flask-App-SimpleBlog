from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
    