# coding: utf-8
#
from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .objects import * 
from .models import *