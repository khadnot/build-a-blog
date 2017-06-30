from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:2Funky44@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.VARCHAR(max))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/blog', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        title_name = request.form['title']
        new_post = request.form['blog']

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    title = request.form['title']
    new_entry = request.form['entry']
    return render_template('new_post.html', title=title, new_entry=new_entry)



    if __name__ == '__main__':
        app.run()
