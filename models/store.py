# -*- coding: utf-8 -*-

from db import db

class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel',lazy='dynamic')
    # lazy='dynamic' helps in not creating an object for all the items Created
    # otherwise evrytime when an item is created an associated object is created for it

    def __init__(self,name):
        self.name = name

    def json(self):
        return {'name':self.name,'items':[items.json() for items in self.items.all()]}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() #similar to Select * from items where name=name limit 1

    #this works both for insert and update, SQLAlchemy upserts using add
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
