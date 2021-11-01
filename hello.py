from flask import Flask, render_template

app = Flask(__name__)

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
def hello():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return 'About page'


if __name__ == '__main__':
    app.run(debug=True)
