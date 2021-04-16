# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:06:49 2021

@author: rrp000d
"""

from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username,password):
    user = UserModel.find_by_username(username)
#    if user and user.password == password:
    if user and safe_str_cmp(user.password,password):
        return user
    

def identify(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)