#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description:

from flask import Blueprint

home = Blueprint("admin", __name__);

import app.admin.views