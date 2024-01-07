"""
This file contains the functional tests for the routes.
These tests use GETs and POSTs to different URLs to check for the proper behavior.
Resources:
    https://flask.palletsprojects.com/en/1.1.x/testing/ 
    https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/ 
"""
import os
import pytest
from app import create_app, db
from app.Model.models import User, Student, Faculty,Position,Application,Researchfield,Programminglanguage
from config import Config
from werkzeug.security import generate_password_hash
from datetime import datetime, date

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = 'bad-bad-key'
    WTF_CSRF_ENABLED = False
    DEBUG = True
    TESTING = True



@pytest.fixture(scope='module')
def test_client():
    # create the flask application ; configure the app for tests
    flask_app = create_app(config_class=TestConfig)

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()
 
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
 
    yield  testing_client 
    # this is where the testing happens!
 
    ctx.pop()

# def new_user(uname, uemail,passwd):
#     user = User(username=uname, email=uemail)
#     user.set_password(passwd)
#     return user


def init_tags():
    # initialize the tags
    # create research fields
    if Researchfield.query.count() == 0:
        rfields = ['Artifical Intelligence', 'Machine Learning', 'Software Engineering', 'High Performance Computing', 'Distributed and Networked Systems', 'Data Science', 'Computer Vision']
        for rf in rfields:
            db.session.add(Researchfield(name=rf))
        db.session.commit()

    # create programming languages
    if Programminglanguage.query.count() == 0:
        plangs = ['Python', 'JavaScript', 'Matlab', 'Julia', 'R']
        for pl in plangs:
            db.session.add(Programminglanguage(name=pl))
        db.session.commit()
    return None

@pytest.fixture
def init_database():
    
    db.create_all()

    init_tags()
    if Student.query.count() == 0:  
        # Student 1 
        student1_test = Student(
        username="student1_test",
        email="student1_test@example.com",
        password_hash=generate_password_hash("123"),
        first_name="student1_test_firstname",
        last_name="student1_test_lastname",
        wsu_id=111768903,
        phone_number="1234567890",
        user_type="Student",
        major="Computer Science",
        gpa=3.5,
        expected_graduation=date(2023, 12, 31)
        )
        student1_test.programming_languages.append(Programminglanguage.query.filter_by(id=1).first())
        student1_test.research_fields.append(Researchfield.query.filter_by(id=1).first())
        db.session.add(student1_test)
        db.session.commit()

    if Faculty.query.count() == 0:    
        # Faculty 1
        faculty1_test = Faculty(
        username="faculty1_test@example.com",
        email="faculty1_test@example.com",
        password_hash=generate_password_hash("123"),
        first_name= "faculty1_test_firstname",
        last_name="faculty1_test_lastname",
        wsu_id=987652324,
        phone_number="5555555557",
        user_type="Faculty"
        )
        db.session.add(faculty1_test)
        db.session.commit()

    if Position.query.count() == 0:  
        # Position 1
        position1_test = Position(
        title="Software Engineer",
        description="Develops software applications",
        start_date= datetime(2023, 10, 15, 8, 0, 0), 
        end_date= datetime(2023, 12, 31, 17, 0, 0),  
        commit_time=40,  
        qualification_description="Bachelor's degree in Computer Science required.",
        faculty_id= faculty1_test.id
        )
        position1_test.programming_languages.append(Programminglanguage.query.filter_by(id=2).first())
        position1_test.research_fields.append(Researchfield.query.filter_by(id=2).first())
        db.session.add(position1_test)
        db.session.commit()

    if Application.query.count() == 0:
        # Application 1  
        application1_test = Application(
            statement="Application Statement",
            faculty_name= faculty1_test.username,
            faculty_email=faculty1_test.email,
            studentid=student1_test.id,  
            positionid=position1_test.id,  
            status="Pending",  
        )
        db.session.add(application1_test)
        db.session.commit()    

    yield  # this is where the testing happens!

    db.drop_all()

def test_register_page(test_client,init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is requested (GET)
    THEN check that the response is valid
    """
    # Create a test client using the Flask application configured for testing
    response = test_client.get('/register')
    assert response.status_code == 200
    assert b"Register" in response.data

def test_register(test_client,init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' form is submitted (POST)
    THEN check that the response is valid and the database is updated correctly
    """
    # Create a test client using the Flask application configured for testing
    response = test_client.post('/register', 
                          data=dict(username="john@gmail.com", 
                    email="john@gmail.com", 
                    password = "123",
                    first_name="Kat", 
                    last_name="John",
                    wsu_id="011753385",
                    phone_number="5093394452",
                    user_type="Student",
                    major="Cpts",
                    gpa="3.0"),
                    follow_redirects = True)
    assert response.status_code == 200

def test_invalidlogin(test_client,init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' form is submitted (POST) with wrong credentials
    THEN check that the response is valid and login is refused 
    """
    response = test_client.post('/login', 
                          data=dict(username='sakire', password='12345',remember_me=False),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Invalid username or password" in response.data  #You may update the assertion condition according to the content of your login page. 

def test_login_logout(request,test_client,init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' form is submitted (POST) with correct credentials
    THEN check that the response is valid and login is succesfull 
    """
    response = test_client.post('/login', 
                          data=dict(username='faculty1_test@example.com', password='123'),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Welcome to Connect app!" in response.data  #You may update the assertion condition according to the content of your index page. 

    response = test_client.get('/logout',                       
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Sign In" in response.data
    assert b"Please log in to access this page." in response.data     #You may update the assertion condition according to the content of your  page. 

def test_postPosition(test_client,init_database):
    """
    GIVEN a Flask application configured for testing , after user logs in,
    WHEN the '/postsmile' page is requested (GET)  AND /PostForm' form is submitted (POST)
    THEN check that response is valid and the class is successfully created in the database
    """
    # Retrieve 4 instances of Student, Faculty, Position and Application from the set up function above. 
    student1_test = Student.query.filter_by(id = 1).first()
    faculty1_test = Faculty.query.filter_by(id = 2).first() 
    position1_test = Position.query.filter_by(id = 1).first()
    application1_test = Application.query.filter_by(positionid = position1_test.id).first()
    
    #login
    response = test_client.post('/login', 
                          data=dict(username='faculty1_test@example.com', password='123'),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Welcome to Connect app!" in response.data  
    
    #test the "PostPosition" form 
    response = test_client.get('/postposition')
    assert response.status_code == 200
    assert b"Post new research position" in response.data 
    
    # test post position 
    response = test_client.post('/postposition', 
                          data=dict(title = "Software Artchitecture", description = "Need someone to do software artchitecture",
                             start_date = datetime(2023, 12, 31, 17, 0, 0), end_date = datetime(2024, 12, 31, 17, 0, 0),
                             commit_time = "12",
                             qualification_description = "I am good",
                             faculty_id = faculty1_test.id),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Software Artchitecture" in response.data
    assert b"Need someone to do software artchitecture" in response.data
    assert str(faculty1_test.username).encode() in response.data

    #finally logout
    response = test_client.get('/logout',                       
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Sign In" in response.data

def test_applyPosition(test_client,init_database):
    # Retrieve 4 instances of Student, Faculty, Position and Application from the set up function above. 
    student1_test = Student.query.filter_by(id = 1).first()
    faculty1_test = Faculty.query.filter_by(id = 2).first() 
    position1_test = Position.query.filter_by(id = 1).first()
    application1_test = Application.query.filter_by(positionid = position1_test.id).first()
    
    # login
    response = test_client.post('/login', 
                          data=dict(username=student1_test.username, password='123'),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Welcome to Connect app!" in response.data  
    
    # apply Get Request
    response = test_client.get(f'/apply/{position1_test.id}',                       
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Application Form" in response.data

    # apply Post Request
    response = test_client.post(f'/apply/{position1_test.id}', 
                        data=dict(title = position1_test.title, statement = "short description", faculty_name = position1_test.faculty.username, faculty_email = position1_test.faculty.email,
                              status = 'Pending'),                      
                        follow_redirects = True)
    assert response.status_code == 200
    assert b"Welcome to Connect app!" in response.data
    assert b"You have successfully applied for this position" in response.data
    assert b"Status: Pending" in response.data
    
    