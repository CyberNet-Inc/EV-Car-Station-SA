from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_username:your_password@localhost/ev_charger_db'
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a random secret

db = SQLAlchemy(app)
jwt = JWTManager(app)
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))

class Register(Resource):
    def post(self):
        data = request.get_json()
        hashed_password = generate_password_hash(data['password'])
        new_user = User(username=data['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully.'}, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity={'username': user.username})
            return jsonify(access_token=access_token)
        return {'message': 'Invalid credentials'}, 401

class ChargerStations(Resource):
    @jwt_required()
    def get(self):
        # Secure the endpoint
        return jsonify({"stations": []})

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(ChargerStations, '/stations')

if __name__ == '__main__':
    db.create_all()  # This creates tables
    app.run(debug=True)
