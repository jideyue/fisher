#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Eric.yue

from flask import Blueprint,jsonify
import json
from .model import user_data

#user 为蓝图名称
#__name__ 为蓝图模块名称
#assets 静态文件
#模板文件
user = Blueprint('user', __name__, static_folder="assets", template_folder='templates')

@user.route('/<int:id>', methods=['GET'])
def get(id):
    for user in user_data:
        if user['id'] == id:
            return jsonify(status='success', user=user)

@user.route('/users', methods=['GET'])
def users():
    data = {
        'status': 'success',
        'users': user_data
    }
    return json.dumps(data, ensure_ascii=False, indent=1)