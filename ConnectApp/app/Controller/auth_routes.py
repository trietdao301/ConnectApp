from __future__ import print_function

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from config import Config

from app import db
from app.Model.models import Student, Faculty, User, Position
from app.Controller.auth_forms import RegistrationForm, LoginForm
from app.Controller.forms import PositionForm

bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 

@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    rform = RegistrationForm()
    if rform.validate_on_submit():
        if rform.user_type.data == 'Student':
            user = Student(username=rform.email.data, 
                    email=rform.email.data, 
                    first_name=rform.first_name.data, 
                    last_name=rform.last_name.data,
                    wsu_id=rform.wsu_id.data,
                    phone_number=rform.phone_number.data,
                    user_type=rform.user_type.data,
                    major=rform.major.data,
                    gpa=rform.gpa.data,
                    expected_graduation=rform.expected_graduation.data)
            for rfield in rform.research_field.data:
                user.research_fields.append(rfield)
            for plang in rform.programming_language.data:
                user.programming_languages.append(plang)
        elif rform.user_type.data == 'Faculty':
            user = Faculty(username=rform.email.data, 
                    email=rform.email.data, 
                    first_name=rform.first_name.data, 
                    last_name=rform.last_name.data,
                    wsu_id=rform.wsu_id.data,
                    phone_number=rform.phone_number.data,
                    user_type=rform.user_type.data,
                    department=rform.department.data)
        user.set_password(rform.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('routes.index'))
    return render_template('register.html', form=rform)

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    lform = LoginForm()
    if lform.validate_on_submit():
        user = User.query.filter_by(username=lform.username.data).first()
        if user is None or not user.get_password(lform.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('routes.index'))                
    return render_template('login.html', form=lform)

@login_required
@bp_auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('routes.index'))

@login_required
@bp_auth.route('/profile')
def profile():
    user_id = current_user.id
    user = User.query.filter_by(id=user_id).first()
    if not user:
        flash('User not found.')
        return redirect(url_for('auth.login'))

    student = None
    faculty = None

    if user.user_type == 'Student':
        student = Student.query.filter_by(student_id=user_id).first()
    elif user.user_type == 'Faculty':
        faculty = Faculty.query.filter_by(faculty_id=user_id).first()
        
    return render_template('profile.html', user=user, student=student, faculty=faculty)

