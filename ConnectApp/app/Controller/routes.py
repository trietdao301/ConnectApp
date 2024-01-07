from __future__ import print_function

import sys

from flask import Blueprint, render_template, flash, redirect, url_for, request
from config import Config
from flask_login import login_required, current_user
from flask import current_app as app

from app import db
from app.Model.models import User, Student, Position, Faculty,Application
from app.Controller.forms import PositionForm,ApplicationForm,EditForm

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'

@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET'])
@login_required
def index():
    position = Position.query.order_by(Position.id)
    user = User.query.filter_by(id = current_user.id).first()
    if user.is_student():
        
        student = Student.query.filter_by(student_id = current_user.id).first()
        return render_template('student_index.html', title="Connect App Portal", positions = position.all(), student = student,faculty = None)
    else:
        faculty = Faculty.query.filter_by(faculty_id = current_user.id).first()
        position = position.filter_by(faculty_id = faculty.faculty_id)
        return render_template('faculty_index.html', title="Connect App Portal",positions = position.all(), faculty = faculty,student = None)
    
    #print("!!!!!!!",position,"!!!!!!!", file=sys.stderr)

@bp_routes.route('/apply/<int:position_id>', methods=['GET', 'POST'])
@login_required
def apply(position_id):
    if not current_user.is_student():
        flash('Only student users can access this page')
        return redirect(url_for('routes.index'))
    position = Position.query.filter_by(id = position_id).first()
    student = Student.query.filter_by(id = current_user.id).first()
    # print("!!!!!!!",student,"!!!!!!!")
    aform = ApplicationForm()
    application = Application(title = position.title, statement = aform.statement.data, faculty_name = aform.faculty_name.data, faculty_email = aform.faculty_email.data,
                              status = 'Pending')
    if position is None:
        flash('Invalid position ID')
        return redirect(url_for('routes.index'))
    if aform.validate_on_submit():
        #student applies for the position
        position.apply(student,application)
        db.session.commit()
        flash('You have successfully applied for this position')
        return redirect(url_for('routes.index'))
    return render_template('apply.html', position_id = position_id, form = aform)

@bp_routes.route('/withdraw/<position_id>',methods=['GET','POST'])
@login_required
def withdraw(position_id):
    if not current_user.is_student():
        flash('Only students users can access this page')
        return redirect(url_for('routes.index'))
    the_application = Application.query.filter_by(positionid = position_id, studentid = current_user.id).first()
    if the_application is None:
        flash('Application with id {} is not found'.format(position_id))
        return redirect(url_for('routes.index'))
    db.session.delete(the_application)
    db.session.commit()
    flash('Application has been succesfully withdrawn!')
    return redirect(url_for('routes.index'))

@bp_routes.route('/postposition', methods=['GET', 'POST'])
@login_required
def post_position():
    if current_user.is_student():
        flash('Only faculty users can access this page')
        return redirect(url_for('routes.index'))
    rpform = PositionForm()
    if rpform.validate_on_submit():
        rposition = Position(title = rpform.title.data, description = rpform.description.data,
                             start_date = rpform.start_date.data, end_date = rpform.end_date.data,
                             commit_time = rpform.commit_time.data,
                             qualification_description = rpform.other_qualifications.data,
                             faculty_id = current_user.id)
        for rfield in rpform.research_field.data:
            rposition.research_fields.append(rfield)
        for plang in rpform.programming_language.data:
            rposition.programming_languages.append(plang)
        db.session.add(rposition)
        db.session.commit()
        flash('New research position has been created!')
        return redirect(url_for('routes.index'))
    return render_template('create.html', form = rpform)

@bp_routes.route('/delete/<int:positionid>', methods=['GET','POST'])
@login_required
def delete_position(positionid):
    if current_user.is_student():
        flash('Only faculty users can access this page')
        return redirect(url_for('routes.index'))
    position = Position.query.filter_by(id = positionid).first()
    if position is None:
        flash('Invalid position ID')
        return redirect(url_for('routes.index'))
    if position.faculty_id != current_user.faculty_id:
        flash('This position does not belong to you!')
        return redirect(url_for('routes.index'))
    for rf in position.research_fields:
        position.research_fields.remove(rf)
    for pl in position.research_fields:
        position.programming_languages.remove(pl)
    for application in position.submissions:
        application.status = 'Position is not available'
        application.positionid = None
    db.session.delete(position)
    db.session.commit()
    flash('You have successfully deleted this position')
    return redirect(url_for('routes.index'))

@bp_routes.route('/applicants/<positionid>', methods=['GET'])
@login_required
def applicants(positionid):
    if current_user.is_student():
        flash('Only faculty users can access this page')
        return redirect(url_for('routes.index'))
    theposition = Position.query.filter_by(id = positionid).first()
    if theposition.faculty_id != current_user.faculty_id:
        flash('This position does not belong to you!')
        return redirect(url_for('routes.index'))
    return render_template('applicants.html', title = 'Position Applicants', current_position = theposition)

@bp_routes.route('/applicants/<positionid>/qualification/<studentid>', methods=['GET'])
@login_required
def qualification(positionid,studentid):
    if current_user.is_student():
        flash('Only faculty users can access this page')
        return redirect(url_for('routes.index'))
    theposition = Position.query.filter_by(id = positionid).first()
    if theposition.faculty_id != current_user.faculty_id:
        flash('This position does not belong to you!')
        return redirect(url_for('routes.index'))
    thestudent= Student.query.filter_by(student_id = studentid).first()
    return render_template('qualification.html', title = 'Qualification',positionid = positionid, student = thestudent)

@bp_routes.route('/applicants/<positionid>/qualification/<studentid>/application', methods=['GET','POST'])
@login_required
def application(positionid,studentid):
    aform  = ApplicationForm()
    if current_user.is_student():
        flash('Only faculty users can access this page')
        return redirect(url_for('routes.index'))
    theposition = Position.query.filter_by(id = positionid).first()
    if theposition.faculty_id != current_user.faculty_id:
        flash('This position does not belong to you!')
        return redirect(url_for('routes.index'))
    theapplication = Application.query.filter_by(positionid = positionid).filter_by(studentid = studentid).first()
    aform.statement.data = theapplication.statement
    aform.faculty_name.data = theapplication.faculty_name
    aform.faculty_email.data = theapplication.faculty_email
    return render_template('application.html', title = 'Application',positionid = positionid, studentid = studentid,application = theapplication,form=aform)

@bp_routes.route('/applicants/<positionid>/qualification/<studentid>/application/approve', methods=['GET','POST'])
@login_required
def approve(studentid,positionid):
    if current_user.is_student():
        flash('Only faculty users can access this page')
        return redirect(url_for('routes.index'))
    theposition = Position.query.filter_by(id = positionid).first()
    if theposition.faculty_id != current_user.faculty_id:
        flash('This position does not belong to you!')
        return redirect(url_for('routes.index'))
    # print("!!!!!!!",studentid)
    theapplication = Application.query.filter_by(positionid = positionid).filter_by(studentid = studentid).first()
    theapplication.status = 'Approved for Interview'
    db.session.commit()
    return redirect(url_for('routes.applicants',positionid = positionid))

@bp_routes.route('/applicants/<positionid>/qualification/<studentid>/application/hire', methods=['GET','POST'])
@login_required
def hire(studentid,positionid):
    if current_user.is_student():
        flash('Only faculty users can access this page')
        return redirect(url_for('routes.index'))
    theposition = Position.query.filter_by(id = positionid).first()
    if theposition.faculty_id != current_user.faculty_id:
        flash('This position does not belong to you!')
        return redirect(url_for('routes.index'))
    theapplication = Application.query.filter_by(positionid = positionid).filter_by(studentid = studentid).first()
    theapplication.status = 'Hired'
    db.session.commit()
    return redirect(url_for('routes.applicants',positionid = positionid))

@bp_routes.route('/applicants/<positionid>/qualification/<studentid>/application/reject', methods=['GET','POST'])
@login_required
def reject(studentid,positionid):
    if current_user.is_student():
        flash('Only faculty users can access this page')
        return redirect(url_for('routes.index'))
    theposition = Position.query.filter_by(id = positionid).first()
    if theposition.faculty_id != current_user.faculty_id:
        flash('This position does not belong to you!')
        return redirect(url_for('routes.index'))
    theapplication = Application.query.filter_by(positionid = positionid).filter_by(studentid = studentid).first()
    theapplication.status = 'Not hired'
    db.session.commit()
    return redirect(url_for('routes.applicants',positionid = positionid))

@bp_routes.route('/editprofile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user = User.query.filter_by(id = current_user.id).first()
    if user.is_student():
        student = Student.query.filter_by(student_id = current_user.id).first()
        eform = EditForm(obj=student)
    else:
        faculty = Faculty.query.filter_by(faculty_id = current_user.id).first()
        eform = EditForm(obj=faculty)
    if eform.validate_on_submit():
        
        if eform.password.data != None and eform.password2.data != "":
            user.set_password(eform.password.data)
            print("eform.password.data", f"2{eform.password.data}2" )
        print(user.password,"what is this")
        user.first_name = eform.first_name.data
        user.last_name = eform.last_name.data
        user.wsu_id = eform.wsu_id.data
        user.phone_number = eform.phone_number.data
        user.user_type = eform.user_type.data
        if user.is_student():
            student.major = eform.major.data
            student.gpa = eform.gpa.data
            student.expected_graduation = eform.expected_graduation.data
            student.prior_exp = eform.prior_exp.data
            student.research_fields = []
            student.programming_languages = []
            for rfield in eform.research_field.data:
                student.research_fields.append(rfield)
            for plang in eform.programming_language.data:
                student.programming_languages.append(plang)
        else:
            faculty.department = eform.department.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('auth.profile'))
    elif request.method == 'GET':
        eform.username.data = user.username
        print(user.username, "!!!!!!!!")
        eform.first_name.data = user.first_name
        eform.last_name.data = user.last_name
        eform.wsu_id.data = user.wsu_id
        eform.phone_number.data = user.phone_number
        eform.user_type.data = user.user_type
        if user.is_student():
            eform.major.data = student.major
            eform.gpa.data = student.gpa
            eform.expected_graduation.data = student.expected_graduation
            eform.prior_exp.data = student.prior_exp
            eform.research_field.data = student.research_fields
            eform.programming_language.data = student.programming_languages
        else:
            eform.department.data = faculty.department
    return render_template('edit_profile.html', title='Edit Profile', form=eform)