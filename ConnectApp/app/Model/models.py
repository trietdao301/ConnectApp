from app import db, login

from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

position_researchfield = db.Table('position_researchfield',
                db.Column('position_id', db.Integer, db.ForeignKey('position.id')),
                db.Column('researchfield_id', db.Integer, db.ForeignKey('researchfield.id')))

position_programminglanguage = db.Table('position_programminglanguage',
                db.Column('position_id', db.Integer, db.ForeignKey('position.id')),
                db.Column('programminglanguage_id', db.Integer, db.ForeignKey('programminglanguage.id')))

student_researchfield = db.Table('student_researchfield',
                db.Column('student_id', db.Integer, db.ForeignKey('student.student_id')),
                db.Column('researchfield_id', db.Integer, db.ForeignKey('researchfield.id')))

student_programminglanguage = db.Table('student_programminglanguage',
                db.Column('student_id', db.Integer, db.ForeignKey('student.student_id')),
                db.Column('programminglanguage_id', db.Integer, db.ForeignKey('programminglanguage.id')))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#  User (id, username, password_hash, lastname, name, WSU ID, email, phone, user_type(String)) 
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index =True)
    email = db.Column(db.String(120), unique = True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    wsu_id = db.Column(db.Integer, unique = True)
    phone_number = db.Column(db.String, unique = True)
    user_type = db.Column(db.String(50))  # user_type are 'Student' and 'Faculty'
    password = ""
    
    __mapper_args__ = {
       'polymorphic_identity':'User',
       'polymorphic_on':user_type
   }
    
    def __repr__(self):
        return '<ID {} - Username {}>'.format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        self.password = password

    def get_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_student(self):
        if self.user_type == 'Student':
            return True
        return False
    
    def display_phone_number(self):
        return '({})'.format(self.phone_number[0:3]) + ' {}-'.format(self.phone_number[3:6]) + self.phone_number[6:]


class Student(User):   
    __tablename__ = 'student'
    __mapper_args__ = {
        'polymorphic_identity':'Student',
    }
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    major = db.Column(db.String(64))
    gpa = db.Column(db.Float)
    expected_graduation = db.Column(db.Date, index=True, default= None)
    research_fields = db.relationship(
        'Researchfield', secondary = student_researchfield,
        primaryjoin = (student_researchfield.c.student_id == student_id),
        backref = db.backref('student_researchfield', lazy = 'dynamic'),
        lazy = 'dynamic'
    )
    programming_languages = db.relationship(
        'Programminglanguage', secondary = student_programminglanguage,
        primaryjoin = (student_programminglanguage.c.student_id == student_id),
        backref = db.backref('student_programminglanguage', lazy = 'dynamic'),
        lazy = 'dynamic'
    )
    prior_exp = db.Column(db.String(1500))
    applications = db.relationship('Application', back_populates='studentsapplied', lazy='dynamic')

    def has_application_for_position(self, positionid):
        appli = Application.query.filter_by(studentid = self.student_id, positionid = positionid).first()
        if appli is None:
            return False
        return True
    
    def get_application(self, positionid):
        appli = Application.query.filter_by(studentid = self.student_id, positionid = positionid).first()
        return appli
    
    def check_if_appliactions_for_list_out_is_none(self,positionid):
        appli1 = Application.query.filter_by(studentid = self.student_id)
        appli2 = Application.query.filter(Application.positionid != positionid)
        appli3 = Application.query.filter(Application.positionid == None)
        uappli = appli2.union(appli3)
        appli = appli1.intersect(uappli).first()
        if appli is None:
            return True
        return False

    def get_applications_for_list_out(self,positionid):
        appli1 = Application.query.filter_by(studentid = self.student_id)
        appli2 = Application.query.filter(Application.positionid != positionid)
        appli3 = Application.query.filter(Application.positionid == None)
        uappli = appli2.union(appli3)
        appli = appli1.intersect(uappli).all()
        return appli

    
class Faculty(User): 
    faculty_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)  
    department = db.Column(db.String(64)) 


    __tablename__ = 'faculty'
    __mapper_args__ = {
       'polymorphic_identity':'Faculty',
   }
    def __repr__(self):
         return "<id: {} - username: {}>".format(self.faculty_id ,self.username)
     
class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(1500))
    start_date = db.Column(db.DateTime, index=True, default= None)
    end_date = db.Column(db.DateTime, index=True, default= None)
    commit_time = db.Column(db.Integer)
    research_fields = db.relationship(
        'Researchfield', secondary = position_researchfield,
        primaryjoin = (position_researchfield.c.position_id == id),
        backref = db.backref('position_researchfield', lazy = 'dynamic'),
        lazy = 'dynamic'
    )
    programming_languages = db.relationship(
        'Programminglanguage', secondary = position_programminglanguage,
        primaryjoin = (position_programminglanguage.c.position_id == id),
        backref = db.backref('position_programminglanguage', lazy = 'dynamic'),
        lazy = 'dynamic'
    )
    qualification_description = db.Column(db.String(1500))
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.faculty_id'))  # Please don't fix this line
    faculty = db.relationship('Faculty', backref='positions')                # Please don't fix this line
    submissions = db.relationship('Application', back_populates='positionsapplied', lazy='dynamic')
    def __repr__(self):
        return "<id: {} - title: {}>".format(self.id,self.title)
    #apply to position
    def apply (self, student,application):
        if not self.has_applied(student):
            application.studentsapplied = student
            self.submissions.append(application)
            db.session.add(application)
            db.session.commit()
            
    def has_applied(self, student):
        return Application.query.filter_by(positionid=self.id).filter_by(studentid=student.student_id).count() > 0

    def get_research_fields(self):
        return self.research_fields
    
    def get_programming_languages(self):
        return self.programming_languages

class Researchfield(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))

    def __repr__(self):
        return '<Research Field {} - {}>'.format(self.id, self.name)
    
class Programminglanguage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __repr__(self):
        return '<Programming Language {} - {}>'.format(self.id, self.name)
#this is a table that links the student and position tables
class Application(db.Model):
    title = db.Column(db.String(150))
    statement = db.Column(db.String(1500))
    faculty_name = db.Column(db.String(150))
    faculty_email = db.Column(db.String(150))
    studentid = db.Column(db.Integer, db.ForeignKey('student.student_id'),primary_key=True)
    positionid = db.Column(db.Integer, db.ForeignKey('position.id'),primary_key=True,nullable=True)
    studentsapplied = db.relationship('Student')
    positionsapplied = db.relationship('Position')
    status = db.Column(db.String(30)) # Pending, Approved for Interview, Hired
    def __repr__(self):
        return '<Application {} - {}>'.format(self.studentid, self.positionid)

