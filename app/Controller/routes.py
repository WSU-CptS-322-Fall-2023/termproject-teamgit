from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config
from app import db
from app.Controller.forms import ReasearchPostForm
bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET'])
def index():
    return render_template('index.html')



@bp_routes.route('/addReasearch', methods=['GET','POST'])
def AddReasearchPost():
    cform = ReasearchPostForm()
    if cform.validate_on_submit():
        print('good')
    return render_template('createRpost.html',form = cform)