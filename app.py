from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request, json
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
    data = request.get_json(force=True)
    if request.method == "POST" and data:
        user = User(name = data.get('name'),points = data.get('points'), user_type = data.get('user_type'))
        db.session.add(user)
        db.session.commit()
        all_users = User.query.order_by(User.points.desc()).filter_by(user_type = "hwdykmq").limit(5).all()
        
#         for user in all_users:
            
        data = {'data':all_users}
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    else:
        data = {'data':"Error"}
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response


# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')




if __name__ == '__main__':
    app.run(debug=True)
