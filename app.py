from flask import Flask,request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(15))
    category = db.Column(db.String(15), unique = False)
    expiration = db.Column(db.Integer, unique = False)

    def __init__(self, name, category, expiration):
        self.name = name
        self.category = category
        self.expiration = expiration

class ItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'category', 'expiration')

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

#  End point for creating a new item.

@app.route('/item', methods = ['POST'])
def add_item():
    name = request.json['name']
    category = request.json['category']
    expiration = request.json['expiration']

    new_item = Item(name,category,expiration)

    db.session.add(new_item)
    db.session.commit()

    item = Item.query.get(new_item.id)

    return item_schema.jsonify(item)
#  End point for creating a new item

@app.route("/items", methods=["GET"])
def get_items():
    all_items = Item.query.all()
    result = items_schema.dump(all_items) 
    return jsonify(result)

# End point for getting all items

@app.route("/item/<id>", methods=["GET"])
def get_item(id):

    item = Item.query.get(id)

    return item_schema.jsonify(item)

#  End point for getting a item


@app.route("/item/<id>", methods=["PUT"])
def update_item(id):
    item = Item.query.get(id)
    name = request.json['name']
    category = request.json['category']
    expiration = request.json['expiration']

    item.name = name
    item.category = category
    item.expiration = expiration

    db.session.commit()
    return item_schema.jsonify(item)

#  End point for updating a item

@app.route("/item/<id>", methods=["DELETE"])
def delete_item(id):
    item = Item.query.get(id)
    
    db.session.delete(item)
    db.session.commit()

    return item_schema.jsonify(item)

# End point for deleting a item 

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)