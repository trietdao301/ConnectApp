from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TextAreaField,PasswordField
from wtforms.validators import  DataRequired, Length, Optional,EqualTo
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput

from app.Model.models import User, Student, Faculty, Position, Researchfield, Programminglanguage

def get_research_fields():
    return Researchfield.query.all()

def get_rfield_name(rfield):
    return rfield.name

def get_programming_languages():
    return Programminglanguage.query.all()

def get_plang_name(plang):
    return plang.name

class PositionForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=150)])
    description = TextAreaField('Description', validators=[DataRequired(),Length(max=1500)])
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    commit_time = StringField('Required Time Commitment', validators=[DataRequired()])
    research_field = QuerySelectMultipleField('Research Field(s)',
                                                    query_factory = get_research_fields, 
                                                    get_label = get_rfield_name,
                                                    widget = ListWidget(prefix_label = False),
                                                    option_widget = CheckboxInput())
    programming_language = QuerySelectMultipleField('Programming Language(s)',
                                                    query_factory = get_programming_languages, 
                                                    get_label = get_plang_name,
                                                    widget = ListWidget(prefix_label = False),
                                                    option_widget = CheckboxInput())
    other_qualifications = TextAreaField('Other Qualifications', validators=[Length(max=1500)])
    submit = SubmitField('Post')

class ApplicationForm(FlaskForm):
    statement = TextAreaField('Statement', validators=[DataRequired(), Length(max=1500)])
    faculty_name = StringField('Name of Faculty', validators=[DataRequired(), Length(max=150)])
    faculty_email = StringField('Email of Faculty', validators=[DataRequired(), Length(max=150)])
    submit = SubmitField('Submit')
class EditForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    password2 = PasswordField('Repeat Password', validators=[EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    wsu_id = StringField('WSU ID', validators=[DataRequired(), Length(min=8,max=9)])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10,max=10)])
    user_type = SelectField('User Type', choices=[('', 'Please select one'), ('Student', 'Student'), ('Faculty', 'Faculty')],
                            validators=[DataRequired()], 
                            render_kw={"placeholder": "Please select one"},
                            coerce=str)
    
    # Student
    major = StringField('Major', validators=[Optional()])
    gpa = StringField('GPA', validators=[Optional()])
    expected_graduation = DateField('Expected Graduation', format='%Y-%m-%d', validators=[Optional()])
    research_field = QuerySelectMultipleField('Research Field(s)',
                                                    query_factory = get_research_fields, 
                                                    get_label = get_rfield_name,
                                                    widget = ListWidget(prefix_label = False),
                                                    option_widget = CheckboxInput())
    programming_language = QuerySelectMultipleField('Programming Language(s)',
                                                    query_factory = get_programming_languages, 
                                                    get_label = get_plang_name,
                                                    widget = ListWidget(prefix_label = False),
                                                    option_widget = CheckboxInput())
    prior_exp = TextAreaField('Prior Research Experience', validators=[Length(max=1500)])

    # Faculty
    department = StringField('Department', validators=[Optional()])
    submit = SubmitField('Submit')
