import warnings
warnings.filterwarnings("ignore")
import os
basedir = os.path.abspath(os.path.dirname(__file__))

from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.Model.models import User, Student, Faculty, Position, Researchfield, Programminglanguage, Application
from config import Config
from werkzeug.security import generate_password_hash
from datetime import datetime, date

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ROOT_PATH = '..//'+basedir
    
class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
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
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    # Testing Position model involes testing apply, has_applied, get_research_fields, get_programming_languages functions
    def test_position_model(self):   
        
        # Retrieve 4 instances of Student, Faculty, Position and Application from the set up function above. 
        student1_test = Student.query.filter_by(id = 1).first()
        faculty1_test = Faculty.query.filter_by(id = 2).first() 
        position1_test = Position.query.filter_by(id = 1).first()
        application1_test = Application.query.filter_by(positionid = position1_test.id).first()
        
        # Test Position Model.
        self.assertEqual(position1_test.faculty_id, faculty1_test.id)
        self.assertEqual(position1_test.title, "Software Engineer")
        self.assertEqual(position1_test.description, "Develops software applications")
        
        # Test get_research_fields
        self.assertEqual(position1_test.get_research_fields().first().name, "Machine Learning")
        
        # Test get_programming_languages
        self.assertEqual(position1_test.get_programming_languages().first().name, "JavaScript")

        # Test Apply method. 
        position1_test.apply(student1_test,application1_test)
        self.assertEqual(application1_test.studentsapplied, student1_test)
        self.assertEqual(position1_test.has_applied(student1_test), True)
    
    
    # Testing Student Model involves testing: has_application_for_position, get_application, check_if_appliactions_for_list_out_is_none
    # and get_applications_for_list_out function 
    def test_student_model(self):
        # Retrieve 4 instances of Student, Faculty, Position and Application from the set up function above. 
        student1_test = Student.query.filter_by(id = 1).first()
        faculty1_test = Faculty.query.filter_by(id = 2).first() 
        position1_test = Position.query.filter_by(id = 1).first()
        application1_test = Application.query.filter_by(positionid = position1_test.id).first()
        
        # Test Student Model.
        self.assertEqual(student1_test.id, 1)
        self.assertEqual(student1_test.major, "Computer Science")
        self.assertEqual(student1_test.gpa, 3.5)

        # Test functions
        self.assertEqual(student1_test.has_application_for_position(position1_test.id), True)
        self.assertEqual(student1_test.get_application(position1_test.id),application1_test)
        self.assertEqual(student1_test.check_if_appliactions_for_list_out_is_none(position1_test.id),True)
        self.assertEqual(student1_test.get_applications_for_list_out(position1_test.id),[])
    
    # Test User Model involves testing get and set password functions
    def test_user_model(self):
        # Retrieve 4 instances of Student, Faculty, Position and Application from the set up function above. 
        student1_test = Student.query.filter_by(id = 1).first()
        faculty1_test = Faculty.query.filter_by(id = 2).first() 
        position1_test = Position.query.filter_by(id = 1).first()
        application1_test = Application.query.filter_by(positionid = position1_test.id).first()
        
        self.assertEqual(student1_test.get_password("123"), True)
        student1_test.set_password("12345")
        self.assertEqual(student1_test.password, "12345")
        self.assertEqual(student1_test.is_student(), True)
if __name__ == '__main__':
    unittest.main(verbosity=2)