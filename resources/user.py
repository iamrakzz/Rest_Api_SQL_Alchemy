# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:05:20 2021

@author: rrp000d
"""
import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                            type=str,
                            required=True,
                            help='This filed cannot be blank'
                            )
    parser.add_argument('password',
                            type=str,
                            required=True,
                            help='This filed cannot be blank'
                            )
    def post(self):

        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message":"A user with the given username already exists!"},400

        user = UserModel(**data)
        user.save_to_db()

        return {"message":"User Created Succesfully."},201
