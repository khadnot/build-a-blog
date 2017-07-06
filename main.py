from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:2Funky44@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/')
def index():
    return redirect('/blog')

@app.route('/newpost', methods=['POST', 'GET'])
def add_post():
    title_error = ''
    post_error = ''
    error_check = False

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        if title == '':
            title_error = "Please enter a title"
            error_check = True
        if body == '':
            post_error = "Please enter a blog post"
            error_check = True
        if error_check == True:
            return render_template('new_post.html', title_error=title_error, post_error=post_error)

        new_blog = Blog(title,body)
        db.session.add(new_blog)
        db.session.commit()
        return redirect('/blog')

    else:
        return render_template('new_post.html')


@app.route('/blog')
def new_post():
    blogs = Blog.query.all()
    if request.args.get('id'):
        id = int(request.args.get('id'))
        title = blogs[id-1].title
        body = blogs[id-1].body
        return render_template('single_post.html', title=title, body=body)
    return render_template('blog.html', blogs=blogs)

if __name__ == '__main__':
    app.run()
