# coding=utf-8 
# /usr/bin/env python
from flask import Blueprint,render_template

route_user = Blueprint('user_page',__name__)

@route_user.route('/login')
def login():
    return render_template("user/login.html")