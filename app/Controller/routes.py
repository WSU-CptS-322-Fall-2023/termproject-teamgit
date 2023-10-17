from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user
from config import Config
from app import db
from app.Controller.forms import ReasearchPostForm, SortForm, ApplicationForm
from app.Model.models import ResearchPost
bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@bp_routes.route('/sindex', methods=['GET', 'POST'])
def sindex():

    posts = ResearchPost.query.order_by(ResearchPost.timestamp.desc())
    
    
    sform = SortForm()
#    if sform.validate_on_submit():
#        if sform.myposts.data is True:
#            posts = current_user.get_user_posts().order_by(ResearchPost.timestamp.desc())

    return render_template('sindex.html', posts=posts,form=sform)

@bp_routes.route('/findex', methods=['GET'])
def findex():

    posts = ResearchPost.query.order_by(ResearchPost.timestamp.desc())
#   posts = current_user.get_user_posts().order_by(ResearchPost.timestamp.desc())

    return render_template('findex.html', posts=posts)

@bp_routes.route('/apply', methods=['GET', 'POST'])
def apply():
    
    form = ApplicationForm()
    if form.validate_on_submit():
        
        flash('Application submitted!', 'success')
        return redirect(url_for('apply'))  # Redirect to a success page or back to the form page

    return render_template('apply.html', form=form)  # Pass the form to the template



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

