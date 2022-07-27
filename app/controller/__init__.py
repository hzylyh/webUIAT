# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/5/10 14:25
LastEditors: John Holl
LastEditTime: 2022/5/10 14:25
"""
from flask import Blueprint

api = Blueprint('api', __name__)

from . import dashboard, engine, case_manage, project_manage, page_manage, po_manage, case_step_manage
