# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/5/10 13:43
LastEditors: John Holl
LastEditTime: 2022/5/10 13:43
"""

from flask import Flask


def create_app():
    app = Flask(__name__)

    # from app.ui import ui as ui_blueprint
    # app.register_blueprint(ui_blueprint)

    from app.controller import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/uiAtApi')

    return app
