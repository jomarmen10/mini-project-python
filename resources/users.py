from flask import jsonify, Blueprint
from flask_restful import (Resource, Api, reqparse, fields, marshal, marshal_with, url_for)

import models

user_fields = {
    'id': fields.Integer,
    'username': fields.String
}

class UserList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument(
            'username',
            required=False,
            help='username does not exist',
            location=['form', 'json']
        )
        super().__init()
    
    def get(self):
        return jsonify({'users': [{'username': 'Franklin'}]})

    def post(self):
        args = self.reqparse.parse_args()
        print(args, '<------ args (req.body)')
        user = models.User.create(**args)
        return jsonify({'users': [{'username': 'Franklin'}]})


class Dog(Resource):
    def get(self, id):
        return jsonify({'username': 'Franklin'})
    
    def put(self, id):
        return jsonify({'username': 'Franklin'})

    def delete(self, id):
        return jsonify({'username': 'Franklin'})




users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(
    UserList,
    '/users'
)

