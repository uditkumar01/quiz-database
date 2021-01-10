from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
# from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676djkjhkffdffdvvbjtigbnbfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    user_type = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.user_type}', '{self.points}')"


@app.route("/")
@app.route("/home",methods = ["GET","POST"])
def save_user():
    if True:
        print(request.method, request.form)
        user = User(name = "yy",points = 2, user_type = "hey")
        db.session.add(user)
        db.session.commit()

        return "Done"
    else:
        return "error"


# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')




if __name__ == '__main__':
    app.run(debug=True)
