from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config
from app import db
from app.Controller.forms import ReasearchPostForm
from app.Model.models import ResearchPost
bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/sindex', methods=['GET'])
def sindex():
    posts = ResearchPost.query.order_by(ResearchPost.timestamp.desc())
    return render_template('sindex.html', posts=posts)


@bp_routes.route('/findex', methods=['GET'])
def findex():
    return render_template('findex.html')

@bp_routes.route('/addReasearch', methods=['GET','POST'])
def AddReasearchPost():
    cform = ReasearchPostForm()
    if cform.validate_on_submit():
        item = ResearchPost()
        item.title = cform.title.data
        item.Description = cform.description.data
        item.Major = cform.major.data
        item.Qualifiications = cform.qualifications.data
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('routes.findex'))
    
    return render_template('createRpost.html',form = cform)

