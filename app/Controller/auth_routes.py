from __future__ import print_function
import sys
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user,login_required
from config import Config
from app import db
from app.Controller.auth_forms import FacultyRegForm, StudentRegForm, LoginForm
from app.Model.models import Faculty, Student, User

bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 

@bp_auth.route('/faculty_reg', methods=['GET','POST'])
def faculty_reg():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    rform= FacultyRegForm()
    if rform.validate_on_submit():
        faculty= Faculty(username=rform.username.data, firstname=rform.firstname.data,
                         lastname=rform.lastname.data, title=rform.title.data,
                         email=rform.email.data, user_type="Faculty")
        faculty.set_password(rform.password.data)
        db.session.add(faculty)
        db.session.commit()
        flash('Congrats, You are now a registered faculty member')
        return redirect(url_for('routes.index'))
    return render_template('FRegister.html',form=rform)

@bp_auth.route('/student_reg', methods=['GET','POST'])
def student_reg():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    rform= StudentRegForm()
    if rform.validate_on_submit():
        student= Student(username=rform.username.data, firstname=rform.firstname.data,
                         lastname=rform.lastname.data, GPA=rform.GPA.data,
                         email=rform.email.data, Major = rform.Major.data, Skills = rform.Skills.data, Year = rform.Year.data,user_type="Student")
        student.set_password(rform.password.data)
        db.session.add(student)
        db.session.commit()
        flash('Congrats, You are now a registered student member')
        return redirect(url_for('routes.index'))
    return render_template('SRegister.html',form=rform)


@bp_auth.route('/', methods=['GET'])
@bp_auth.route('/login', methods =['GET','POST'])
def login():
    if current_user.is_authenticated:
        if current_user.user_type=="Student":
            return redirect(url_for('routes.index'))
        else:
            return redirect(url_for('routes.index'))
    lform= LoginForm()
    if lform.validate_on_submit():
        user = User.query.filter_by(username=lform.username.data).first()
        if(user is None) or (user.get_password(lform.password.data)==False):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=lform.remember_me.data)

        if current_user.user_type=="Student":
            return redirect(url_for('routes.index'))
        else:
            return redirect(url_for('routes.index'))
        
    return render_template('login.html',form=lform)

@bp_auth.route('/logout', methods =['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))