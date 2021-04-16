# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:52:31 2021

@author: rrp000d
"""

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identify
from resources.user import UserRegister
from resources.item import Item,ItemList
from resources.store import Store,StoreList

app = Flask(__name__)
#searches for sqlite database in the root folder of the file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#this only disables track modifications of flask_sqlalchemy and not main SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'test'
api = Api(app)

jwt = JWT(app,authenticate,identify) #/auth


#this is same as decorating the get function with app.route
api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')

api.add_resource(UserRegister,'/register')

#debug=True gives more information on execution
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
