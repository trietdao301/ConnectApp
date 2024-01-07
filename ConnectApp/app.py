from app import create_app, db
from app.Model.models import User, Student, Faculty, Position, Researchfield, Programminglanguage, Application
from datetime import datetime, date
from werkzeug.security import generate_password_hash
import sys
      
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': app.db, 'User': User, 'Student' : Student}

@app.before_request
def initDB(*args, **kwargs):
    with app.app_context():
        db.create_all()
        
        # create research fields
        if Researchfield.query.count() == 0:
            rfields = ['Artifical Intelligence', 'Machine Learning', 'Software Engineering', 'High Performance Computing', 'Distributed and Networked Systems', 'Data Science', 'Computer Vision', 'Natural Language Processing', 'Computer Graphics', 'Human-Computer Interaction', 'Computer Security', 'Computer Architecture', 'Computer Networks', 'Database Systems', 'Programming Languages', 'Theory of Computation', 'Operating Systems', 'Robotics', 'Embedded Systems', 'Computational Biology', 'Computational Chemistry', 'Computational Physics', 'Computational Mathematics', 'Computational Economics', 'Computational Finance', 'Computational Sociology', 'Computational Neuroscience', 'Computational Linguistics', 'Computational Musicology', 'Computational Engineering', 'Computational Statistics', 'Computational Social Science', 'Computational Law', 'Computational Humanities', 'Computational Theology', 'Computational Philosophy']
            for rf in rfields:
                db.session.add(Researchfield(name=rf))
            db.session.commit()

        # create programming languages
        if Programminglanguage.query.count() == 0:
            plangs = ['Python', 'JavaScript', 'Matlab', 'Julia', 'R', 'C++', 'Java', 'C', 'C#', 'PHP', 'Go', 'Swift', 'Ruby', 'TypeScript', 'Kotlin', 'Scala', 'Rust', 'Perl', 'Haskell', 'Dart', 'Lua', 'Elixir', 'Clojure', 'Groovy', 'Erlang', 'F#', 'OCaml', 'Scheme', 'Bash', 'Assembly', 'Objective-C', 'VimL', 'CoffeeScript', 'PowerShell', 'TeX', 'Emacs Lisp', 'Racket', 'Crystal', 'D', 'Fortran', 'Haxe', 'Common Lisp', 'Nim', 'Vala', 'Forth', 'Pascal', 'Visual Basic', 'Elm', 'AutoHotkey', 'Coq', 'Dylan', 'Julia', 'Nix', 'PureScript', 'Raku', 'Smalltalk', 'Zig', 'Ada', 'Apex', 'ATS', 'Ceylon', 'Eiffel', 'F*', 'Fantom', 'Frege', 'Idris', 'J', 'Kotlin', 'Kotlin', 'LiveScript', 'Logtalk', 'Mirah', 'Monkey', 'Nemerle', 'NetLogo', 'Oxygene', 'Pike', 'Pony', 'Processing', 'PureBasic', 'PureScript', 'Racket', 'Rebol', 'Red', 'Ring', 'Rust', 'SAS', 'Squirrel', 'Tcl', 'Turing', 'TXL', 'VHDL', 'X10', 'Xojo', 'Zephir']
            for pl in plangs:
                db.session.add(Programminglanguage(name=pl))
            db.session.commit()
            
        # Create 2 Faculty 
        if Faculty.query.count() == 0:
            #1st faculty
            faculty_member1 = Faculty(
            username="faculty@example.com",
            email="faculty@example.com",
            password_hash=generate_password_hash("123"),
            first_name= "member1",
            last_name="Member",
            wsu_id=987652324,
            phone_number="5555555557",
            user_type="Faculty"
            )
            #2nd faculty
            faculty_member2 = Faculty(
            username="triet301@example.com",
            email="triet301@example.com",
            password_hash=generate_password_hash("123"),
            first_name= "member2",
            last_name="Dao",
            wsu_id=300987654,
            phone_number="5565655557",
            user_type="Faculty"
            )
            db.session.add(faculty_member1)
            db.session.add(faculty_member2)
            db.session.commit()
        
        #create 1 student, so that we can apply for positions
        if Student.query.count() == 0:
            # Student 1
            student1 = Student(
            username="student@example.com",
            email="student@example.com",
            password_hash=generate_password_hash("student_password"),
            first_name="someone",
            last_name="Member",
            wsu_id=111768903,
            phone_number="1234567890",
            user_type="Student",
            major="Computer Science",
            gpa=3.5,
            expected_graduation=date(2023, 12, 31)
            )
            student1.programming_languages.append(Programminglanguage.query.filter_by(id=2).first())
            student1.research_fields.append(Researchfield.query.filter_by(id=3).first())
            db.session.add(student1)
            db.session.commit()
            
             # Student 2
            student2 = Student(
            username="student@2.com",
            email="student@2.com",
            password_hash=generate_password_hash("123"),
            first_name= "Kelly",
            last_name="Lim",
            wsu_id=112221222,
            phone_number="1234560000",
            user_type="Student",
            major="Computer Science22222222222222",
            gpa=4,
            expected_graduation=date(2023, 12, 31)
            )
            student2.programming_languages.append(Programminglanguage.query.filter_by(id=1).first())
            student2.research_fields.append(Researchfield.query.filter_by(id=4).first())
            db.session.add(student2)
            db.session.commit()
        print("#######",Student.query.all(),"######",Student.query.count(), file=sys.stderr)
        
        # Create 2 Positions. 
        if Position.query.count() == 0:    
            #1st position
            position1 = Position(
            title="Software Engineer",
            description="Develops software applications.",
            start_date= datetime(2023, 10, 15, 8, 0, 0), 
            end_date= datetime(2023, 12, 31, 17, 0, 0),  
            commit_time=40,  
            qualification_description="Bachelor's degree in Computer Science required.",
            faculty_id= faculty_member1.id
            )
            position1.research_fields.append(Researchfield.query.filter_by(id=1).first())
            position1.research_fields.append(Researchfield.query.filter_by(id=2).first())
            position1.programming_languages.append(Programminglanguage.query.filter_by(id=1).first())
            position1.programming_languages.append(Programminglanguage.query.filter_by(id=2).first())
            position1.programming_languages.append(Programminglanguage.query.filter_by(id=3).first())
            #2nd position
            position2 = Position(
            title="Data Scientist",
            description="Analyzes and models data to extract insights.",
            start_date=datetime(2023, 11, 1, 9, 0, 0),
            end_date=datetime(2024, 3, 31, 18, 0, 0),
            commit_time=35,  # Replace with the number of hours or a relevant value
            qualification_description="Master's degree in Data Science required.",
            faculty_id = faculty_member2.id   # Replace with the actual faculty_id
            )
            position2.research_fields.append(Researchfield.query.filter_by(id=3).first())
            position2.research_fields.append(Researchfield.query.filter_by(id=4).first())
            position2.programming_languages.append(Programminglanguage.query.filter_by(id=4).first())
            position2.programming_languages.append(Programminglanguage.query.filter_by(id=2).first())
            position2.programming_languages.append(Programminglanguage.query.filter_by(id=1).first())
            position2.programming_languages.append(Programminglanguage.query.filter_by(id=5).first())

            db.session.add(position1)
            db.session.add(position2)
            position3 = Position(
            title="Research Scientist",
            description="Researches and develops new technologies.",
            start_date=datetime(2023, 11, 1, 9, 0, 0),
            end_date=datetime(2024, 3, 31, 18, 0, 0),
            commit_time=35,  # Replace with the number of hours or a relevant value
            qualification_description="Master's degree in Data Science required.",
            faculty_id = faculty_member2.id   # Replace with the actual faculty_id
            )
            position3.research_fields.append(Researchfield.query.filter_by(id=6).first())
            position3.research_fields.append(Researchfield.query.filter_by(id=5).first())
            position3.programming_languages.append(Programminglanguage.query.filter_by(id=5).first())
            position3.programming_languages.append(Programminglanguage.query.filter_by(id=6).first())
            position3.programming_languages.append(Programminglanguage.query.filter_by(id=2).first())

            db.session.add(position3)
            db.session.commit()

        #-------------------------- Test use case 12 and 13: --------------------------#  (To test, login = bin301, pass = 123)
        # Create an Application1 instance and connect it to the Position1 and Student1 instance
        if Application.query.count() == 0:  
            
            # Application 1  
            application1 = Application(
                title=position1.title,
                statement="Application Statement",
                faculty_name="Faculty Name",
                faculty_email="faculty_email@example.com",
                studentid=student1.id,  # Link the application to the student1
                positionid=position1.id,  # Link the application to the position1
                status="Pending",  # Set the status 
            )
            # Add the application to the student's applications and positionsapplied lists
            student1.applications.append(application1)
            position1.submissions.append(application1)
            db.session.add(application1)
            db.session.commit()
            
            # Application 2 
            application2 = Application(
                title=position2.title,
                statement="Application Statement",
                faculty_name="Faculty Name",
                faculty_email="faculty_email@example.com",
                studentid=student2.id,  # Link the application to the student2
                positionid=position2.id,  # Link the application to the position2
                status="Pending",  # Set the status 
            )
            # Add the application to the student's applications and positionsapplied lists
            student2.applications.append(application2)
            position2.submissions.append(application2)
            db.session.add(application2)
            db.session.commit()

            # Application 3
            application3 = Application(
                title=position1.title,
                statement="Application Statement",
                faculty_name="Faculty Name",
                faculty_email="faculty_email@example.com",
                studentid=student2.id, # Link the application to the student2
                positionid=position1.id, # Link the application to the position1
                status="Pending" # Set the status
            )
            # add the application to the student's applciations and positionsapplied lists
            student2.applications.append(application3)
            position1.submissions.append(application3)
            db.session.add(application3)
            db.session.commit()
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)