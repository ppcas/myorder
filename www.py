# coding=utf-8 
# /usr/bin/env python
from application import app
from web.controller.index import route_index
from web.controller.user.User import route_user
from web.controller.static import route_static
from web.controller.account.Account import route_account




app.register_blueprint(route_index,url_prefix = '/')
app.register_blueprint(route_user,url_prefix='/user')
app.register_blueprint(route_static,url_prefix='/static')
app.register_blueprint(route_account,url_prefix='/account')