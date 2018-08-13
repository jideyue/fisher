#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Eric.yue
import json

from flask import Blueprint, jsonify

from .model import dept_data

#from app.forms.book import SearchForm

dept = Blueprint('dept', __name__, static_folder="assets", template_folder='templates')

@dept.route('/<int:id>', methods=['GET'])
def get(id):
    for dept in dept_data:
        if int(dept['id']) == id:
            return jsonify(status='success', dept=dept)

    return jsonify(status='failed', msg='dept not found')


@dept.route('/depts', methods=['GET'])
def get_depts():
    data = {
        'status': 'success',
        'depts': dept_data
    }
    return json.dumps(data, ensure_ascii=False, indent=1)