# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:07:16 2021

@author: rrp000d
"""
import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                            type=float,
                            required=True,
                            help='This filed cannot be blank'
                            )
    parser.add_argument('store_id',
                            type=int,
                            required=True,
                            help='Every Item needs a store id!'
                            )
    @jwt_required()
    def get(self,name):

        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {"message":"Item not found!"},404

    def post(self,name):
        #check if the same item is being sent
        if ItemModel.find_by_name(name):
            return {'message':"An item with name '{}'already exists.".format(name)},400

        data = Item.parser.parse_args()
        item = ItemModel(name,data['price'],data['store_id'])#or **data

        try:
            item.save_to_db()
        except:
            return {"message":"An error occured while inserting the item!"},500 #internal server error

        return item.json(),201

    def delete(self,name):

        item = ItemModel.find_by_name(name)

        if item:
            item.delete_from_db()

        return {"message":"Item Deleted!"}

    def put(self,name):
#        data = request.get_json()
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            #create a new item object
            item = ItemModel(name,data['price'],data['store_id']) #or **data
        else:
            #update the price
            item.price = data['price']

        item.save_to_db()
        return item.json()


#create another class to retrieve multiple items
class ItemList(Resource):
    def get(self):
        return {'items':[item.json() for item in ItemModel.query.all()]}
