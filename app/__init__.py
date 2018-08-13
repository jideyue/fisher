#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Eric.yue

from flask import Flask

from user.views import user
from dept.views import dept

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app

def register_blueprint(app):
    app.register_blueprint(user, url_prefix='/user') #register user
    app.register_blueprint(dept, url_prefix='/dept') #register dept