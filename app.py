from flask import Flask, render_template, request, redirect, url_for
from models import db, Post

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html", content=Post.query.all())

@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template("post.html", post=Post.query.get(post_id))

@app.route("/create-post", methods=["GET","POST"])
def create_post():
    if request.method == 'GET':
        return render_template("create_post.html")
    title = request.form['title']
    content = request.form['content']
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete-post/<int:post_id>")
def delete_post(post_id):
    post=Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()