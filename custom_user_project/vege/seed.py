from faker import Faker
fake = Faker()
import random
from .models import *

def create_subject_marks():
    try:
        student_objs = Student.objects.all()  # Fetch all students
        subjects = Subject.objects.all()  # Fetch all subjects
        
        for student in student_objs:
            for subject in subjects:
                # Check if SubjectMarks already exists for this student and subject
                if not SubjectMarks.objects.filter(student=student, subject=subject).exists():
                    # Generate random marks and create a new SubjectMarks entry
                    marks = random.randint(0, 100)
                    SubjectMarks.objects.create(
                        student=student,
                        subject=subject,
                        marks=marks
                    )
    except Exception as e:
        print(f"Error: {e}")


def seed_db(n=10)->None:
    try:
        for i in range(0,10):
            departement_objs = Departement.objects.all()
            random_index = random.randint(0,len(departement_objs)-1)
            departement = departement_objs[random_index]
            student_id = f'STU-0{random.randint(100,999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            student_obj = Student.objects.create(
                departement =departement,
                student_id =student_id_obj,
                student_name =student_name,
                student_email =student_email,
                student_age =student_age,
                student_address =student_address,

            )
    except Exception as e:
        print(e) 