from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from config import Config
from app import db
from app.Controller.forms import ReasearchPostForm, SortForm, ApplicationForm
from app.Model.models import ResearchPost, Apply
bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('index.html')


@bp_routes.route('/sindex', methods=['GET', 'POST'])
@login_required
def sindex():

    posts = ResearchPost.query.order_by(ResearchPost.timestamp.desc())
    
    
    sform = SortForm()
#    if sform.validate_on_submit():
#        if sform.myposts.data is True:
#            posts = current_user.get_user_posts().order_by(ResearchPost.timestamp.desc())

    return render_template('sindex.html', posts=posts,form=sform)

@bp_routes.route('/findex', methods=['GET'])
@login_required
def findex():

    posts = ResearchPost.query.order_by(ResearchPost.timestamp.desc())
#   posts = current_user.get_user_posts().order_by(ResearchPost.timestamp.desc())

    return render_template('findex.html', posts=posts)

@bp_routes.route('/apply/<int:researchpost_id>', methods=['GET', 'POST'])
@login_required
def apply(researchpost_id):
    research_post = ResearchPost.query.get_or_404(researchpost_id)  

    form = ApplicationForm()
    if form.validate_on_submit():
        item = Apply()
        item.research_topic = form.research_topic.data
        item.statement = form.statement.data
        item.faculty_name = form.faculty_name.data
        item.faculty_email = form.faculty_email.data

        item.researchpost_id = researchpost_id  

        db.session.add(item)
        db.session.commit()
        
        flash('You have succesfully applied to the ' + research_post.title + " position", 'success')
        return redirect(url_for('routes.sindex'))  

    return render_template('apply.html', form=form, research_post=research_post)  



@bp_routes.route('/addReasearch', methods=['GET','POST'])
@login_required
def AddReasearchPost():
    cform = ReasearchPostForm()
    if cform.validate_on_submit():
        item = ResearchPost()
        item.title = cform.title.data
        item.Description = cform.description.data
        item.Major = cform.major.data
        item.Qualifications = cform.qualifications.data
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('routes.findex'))
    
    return render_template('createRpost.html',form = cform)


@bp_routes.route('/seeReasearch/<postid>', methods=['GET','POST'])
@login_required
def seeReasearch(postid):
    print(postid)
    thepost = ResearchPost.query.filter_by(id=postid).first()
    print(thepost)
    return render_template('pdetails.html',post = thepost)