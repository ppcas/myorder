# coding=utf-8 
# /usr/bin/env python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from common.libs.UrlManger import UrlManger


import os


class Application(Flask):
    def __init__(self,import_name,template_folder = None,root_path=None):
        super(Application, self).__init__(import_name,template_folder = template_folder,root_path=root_path,static_folder=None)
        self.config.from_pyfile('config/base_setting.py')
        if 'ops_config' in os.environ:
            self.config.from_pyfile('config/%s_setting.py'%os.environ["ops_config"])

        db.init_app(self)

db = SQLAlchemy()
app = Application(__name__,template_folder=os.getcwd()+"/web/templates",root_path=os.getcwd())

manager = Manager(app)


'''
'''
app.add_template_global(UrlManger.buildstaticurl,'buildStaticUrl')
app.add_template_global(UrlManger.buildurl,'buildUrl')
