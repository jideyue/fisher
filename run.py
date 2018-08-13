#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Eric.yue

from app import create_app

#初始化app
app = create_app()

if __name__ == '__main__':
    #print app.url_map
    app.run('0.0.0.0', debug=app.config["DEBUG"], port=8080)