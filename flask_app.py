
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# init app


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,
                                                                    'database')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
database = SQLAlchemy(app)
# Init ma
marshmallow = Marshmallow(app)


class NecklaceStone(database.Model):

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), unique=True)
    country = database.Column(database.String)
    price = database.Column(database.Float)
    carats = database.Column(database.Float)

    def __init__(self, name="No name",
                 mine_place="No name", price=0.0, carats=0.0):
        self.name = name
        self.country = mine_place
        self.price = price
        self.carats = carats


class NecklaceStoneSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'name', 'country', 'price', 'carats')


necklace_stone_schema = NecklaceStoneSchema(strict=True)
necklace_stones_schema = NecklaceStoneSchema(many=True, strict=True)

# default page
@app.route('/')
def greetings():
    return jsonify({'msg': 'OMONPMMPOMONOMONNOMONOMONOMONOM'
                           'route (/necklacestone).'})

# Create stone
@app.route('/necklacestone', methods=['POST'])
def add_stone():
    name = request.json['name']
    country = request.json['country']
    price = request.json['price']
    carats = request.json['carats']

    new_necklace_stone = NecklaceStone(name,
                                       # transparency,
                                       country, price,
                                       carats)
    database.session.add(new_necklace_stone)
    database.session.commit()

    return necklace_stone_schema.jsonify(new_necklace_stone)


@app.route('/necklacestone', methods=['GET'])
def get_all_stones():
    all_stones = NecklaceStone.query.all()
    result = necklace_stones_schema.dump(all_stones)
    return jsonify(result.data)


@app.route('/necklacestone/<id>', methods=['GET'])
def get_stone(id):
    necklace_stone = NecklaceStone.query.get(id)
    return necklace_stone_schema.jsonify(necklace_stone)


@app.route('/necklacestone/<id>', methods=['PUT'])
def update_necklace_stone(id):
    necklace_stone = NecklaceStone.query.get(id)
    name = request.json['name']
    country = request.json['country']
    price = request.json['price']
    carats = request.json['carats']

    necklace_stone.name = name
    necklace_stone.country = country
    necklace_stone.price = price
    necklace_stone.carats = carats

    database.session.commit()

    return necklace_stone_schema.jsonify(necklace_stone)


@app.route('/necklacestone/<id>', methods=['DELETE'])
def delete_necklace_stone(id):
    necklace_stone = NecklaceStone.query.get(id)
    database.session.delete(necklace_stone)
    database.session.commit()
    return necklace_stone_schema.jsonify(necklace_stone)


if __name__ == '__main__':
    app.run(debug=True)

