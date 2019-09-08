from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import app
import json

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='user'
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(255), nullable=False)

    def add_user(_username, _password):
        new_user = User(username=_username, password=_password)
        db.session.add(new_user)
        db.session.commit()

    def get_all_users():
        return User.query.all()

    def get_user(_username):
        return User.query.filter_by(username=_username).first()

    def delete_user(_username):
        User.query.filter_by(username=_username).delete()
        db.session.commit()

    def update_user_password(_username, _password):
        user_to_update = User.query.filter_by(username=_username).first()
        user_to_update.password = _password
        db.session.commit()

    
    def __repr__(self):
        user = {
                'username':self.username,        
                'password':self.password
        }
        return json.dumps(user)
