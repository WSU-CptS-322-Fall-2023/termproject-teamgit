from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from config import Config
from app import db
from app.Controller.forms import ReasearchPostForm, SortForm, ApplicationForm
from app.Model.models import ResearchPost, Apply,Student, researchinterest, appun
bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'



@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    posts = ResearchPost.query.order_by(ResearchPost.timestamp.desc())
    sform= SortForm()
    if current_user.user_type == 'Student':
        if sform.validate_on_submit():
            posts=researchinterest.query.filter_by(name=sform.choices.data).first_or_404()
    else:
        posts=current_user.get_user_posts().order_by(ResearchPost.timestamp.desc())   

    return render_template('index.html', posts=posts,form=sform)

@bp_routes.route('/apply/<int:researchpost_id>', methods=['GET', 'POST'])
@login_required
def apply(researchpost_id):
    
    if current_user.user_type == 'Faculty':
        flash('Only Student members can apply!')
        return redirect(url_for('index'))
    else:
        research_post = ResearchPost.query.get_or_404(researchpost_id)  
        form = ApplicationForm()
        if form.validate_on_submit():
            item = Apply()
            item.research_topic = research_post.title
            item.statement = form.statement.data
            item.faculty_name = form.faculty_name.data
            item.faculty_email = form.faculty_email.data
            item.researchpost_id = researchpost_id  
            item.status = 'Pending'
            current_user.applications.append(item)
            research_post.applications.append(item)
            db.session.add(item)
            db.session.commit()     
            flash('You have succesfully applied to the ' + research_post.title + " position", 'success')
            return redirect(url_for('routes.index'))  
    return render_template('apply.html', form=form, research_post=research_post)  



@bp_routes.route('/addReasearch', methods=['GET','POST'])
@login_required
def AddReasearchPost():

    if current_user.user_type == "Student":
        flash('You cannot access this page!')
        return redirect(url_for('routes.index'))
    else:
        cform = ReasearchPostForm()
        if cform.validate_on_submit():
            item = ResearchPost()
            item.title = cform.title.data
            item.Description = cform.description.data
            item.Major = cform.major.data
            item.Qualifications = cform.qualifications.data
            item.user_id=current_user.id
            for i in cform.tag.data:
                item.interests.append(i)
            for s in cform.tag2.data:
                item.skills.append(s)
            current_user.research_posts.append(item)
            db.session.add(item)
            db.session.commit()
            return redirect(url_for('routes.index'))
    
    return render_template('createRpost.html',form = cform)


@bp_routes.route('/seeReasearch/<postid>', methods=['GET','POST'])
@login_required
def seeReasearch(postid):
    print(postid)
    thepost = ResearchPost.query.filter_by(id=postid).first()
    print(thepost)
    return render_template('pdetails.html',post = thepost)



@bp_routes.route('/viewStudent/<app>/<student>', methods=['GET','POST'])
@login_required
def viewStudent(app,student):
    if current_user.user_type == "Student":
        flash('You cannot access this page!')
        return redirect(url_for('routes.index'))
    else:
        theapp = Apply.query.filter_by(id=app).first()
        theStudent = Student.query.filter_by(id=student).first()
        return render_template('studentdetails.html',user = theStudent,app=theapp)


@bp_routes.route('/applications', methods=['GET','POST'])
@login_required
def applications():

    if current_user.user_type == "Faculty":
        flash('You cannot access this page!')
        return redirect(url_for('routes.index'))
    
    posts=current_user.get_user_app()
    
    return render_template('application.html', user =current_user,posts=posts)

@bp_routes.route('/delete/<post_id>', methods=['DELETE','POST'])
@login_required
def delete(post_id):
    if post_id is not None:
        thepost = ResearchPost.query.filter_by(id=post_id).first()
        for i in thepost.interests:
            thepost.interests.remove(i)
        for s in thepost.skills:
            thepost.skills.remove(s)

        for state in thepost.applications:
            app = appun(research_topic = state.research_topic, statement= state.statement, faculty_name=state.faculty_name, faculty_email=state.faculty_email, user_id =state.students[0].id,status= "Post not available")
            db.session.add(app)
            db.session.commit()

        for state in thepost.applications:
            db.session.delete(state)
        db.session.commit()
        db.session.delete(thepost)
        db.session.commit()
        flash('Your post has been deleted!')
        return redirect(url_for('routes.index'))
    



    
@bp_routes.route('/appresponse/<appid>/<int:choice>', methods=['GET', 'DELETE', 'POST'])
@login_required
def appResponse(appid, choice):
    print(appid)
    App = Apply.query.filter_by(id=appid).first()
    apun = appun.query.filter_by(id=appid).first()
    if choice == 1:
        App.status = 'Hired!'
    elif choice == 2:
        App.status = 'Requested For Interview'
    elif choice == 3:
        App.status = 'Denied'
    elif choice == 4:
        db.session.delete(App)
    else:
        db.session.delete(apun)
    db.session.commit()
    return redirect(url_for('routes.index'))
