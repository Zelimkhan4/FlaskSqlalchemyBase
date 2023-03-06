from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.news import News
from forms.register_form import RegisterForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"


@app.route("/")
def home():
    sess = db_session.create_session()
    news = sess.query(News).all()
    return render_template("home.html", news=news)


@app.route("/register", methods=["POST", "GET"])
def register():
    sess = db_session.create_session()
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.passwordAgain.data:
            return render_template("register_form.html", form=form, message="Пароли не совпадают!")
        if sess.query(User).filter(User.email == form.email.data).first():
            return render_template("register_form.html", form=form, message="Такой пользователь уже есть!")
        user = User(
            name=form.username.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        sess.add(user)
        sess.commit()
        return redirect("/")

    return render_template("register_form.html", form=form)


if __name__ == "__main__":
    db_session.global_init("db/blogs.sqlite3")
    app.run()