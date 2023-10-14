from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config
from app import db
bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/sindex', methods=['GET'])
def sindex():
    return render_template('sindex.html')


@bp_routes.route('/findex', methods=['GET'])
def findex():
    return render_template('findex.html')