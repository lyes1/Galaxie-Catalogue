# coding: utf-8
#
from flask import Blueprint
routes = Blueprint('routes', __name__)

from .generalRoutes import *
from .objectsRoute import * 