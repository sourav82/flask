from flask import Flask
from settings import app
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__='product'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    description=db.Column(db.String(255), nullable=False)
    price=db.Column(db.Float, nullable=False)

    def add_product(_name, _description, _price):
        new_product = Product(name=_name, description=_description, price=_price)
        db.session.add(new_product)
        db.session.commit()

    def get_products(): 
        return Product.query.all()

    def get_product_by_name(_name):
        products = Product.query.filter_by(name.like('%'+_name+'%')).all()
        return products

    def update_product(_name, _description, _price):
        product = Product.query.filter_by(name=_name).filter_by(description=_description).filter_by(price=_price).first()
        product.name = _name
        product.description = _description
        product.price= _price
        db.session.commit()

    def update_product(_name, _description):
        product = Product.query.filter_by(name=_name).filter_by(description=_description).first()
        product.name = _name
        product.description = _description
        db.session.commit()

    def update_product(_name):
        product = Product.query.filter_by(name=_name).first()
        product.name = _name
        db.session.commit()

    def delete_product(_name):
        Product.query.filter_by(name=_name).delete()
        db.session.commit()

    def __repr__(self):
        product={
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "price": self.price
        }
        return json.dumps(product)

