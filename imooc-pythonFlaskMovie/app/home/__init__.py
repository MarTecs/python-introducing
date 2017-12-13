#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description:

from flask import Blueprint

home = Blueprint("home", __name__);

import app.home.views