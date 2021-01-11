from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
# from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    user_type = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.user_type}', '{self.points}')"
    
with app.app_context():
    db.create_all()


# @app.route("/")
@app.route("/save_user",methods = ["GET","POST"])
def save_user():
    data = {'data':"Error"}
    if request.method == "POST":
        data = request.get_json(force=True)
    if request.method == "POST" and data:
        user = User(name = data.get('name'),points = data.get('points'), user_type = data.get('user_type'))
        db.session.add(user)
        db.session.commit()
        all_users = User.query.order_by(User.points.desc()).filter_by(user_type = data.get('user_type')).all()
        users,rank,count = [],-1,0
        for user1 in all_users:
            count+=1
            if rank==-1 and user1.name == data.get('name') and user1.points == data.get('points') and user1.user_type == data.get('user_type'):
                rank = count
            if count<=5:
                users.append({"name":user1.name,"points":user1.points,"user_type":user1.user_type})
            
        data = {'data':users,'rank':rank}
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
