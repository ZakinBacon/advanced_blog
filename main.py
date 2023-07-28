from flask import Flask, request
from flask import render_template
import requests
from post import Post

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/b727a03702b154ce9ceb").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route("/")
def home():
    return render_template('index.html', all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/about_us")
def about_us():
    return render_template('about.html')


@app.route("/contact", methods=["GET", "POST"])
def contact_me():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template('contact.html')

# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#
#     print(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
#     return f"<h1>Succesfully sent your message!</h1>"

if __name__ == "__main__":
    app.run(debug=True)