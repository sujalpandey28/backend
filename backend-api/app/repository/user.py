import time
import random
from fastapi import HTTPException,status
from app import schemas
from sqlalchemy.orm import Session
from app import models

def generate_unique_id(length=12):
    # characters = string.ascii_letters + string.digits
    # unique_id = ''.join(random.choices(characters, k=length))
    # return unique_id

    # Get the current timestamp in milliseconds
    timestamp = int(time.time() * 1000)

    # Generate a random number
    random_number = random.randint(0, 2**20 - 1)  # random 20-bit number

    # Combine timestamp and random number
    combined = (timestamp << 20) | random_number

    # Convert to hexadecimal and ensure it is 10 characters long
    unique_id = hex(combined)[-10:]

    return unique_id

def create_user(request:schemas.create_user,db:Session):
    user_created=models.User(
        user_id= generate_unique_id(),
        name=request.name,
        email=request.email,
        mobile=request.mobile,
        password=request.password
    )
    db.add(user_created)
    db.commit()
    return user_created.user_id

def get_user(user_id:str,db:Session):
    user = db.query(models.User).filter(models.User.user_id==user_id).first()
    if not user :
        raise HTTPException(status_code=404, detail="user not found")
    return {"user_id":user.user_id,
            "name":user.name,
            "email":user.email,
            "phone":user.mobile
            }

def create_university(request:schemas.create_university,db:Session):
    university_created=models.University(
        university_id= generate_unique_id(),
        university_name= request.university_name,
        university_address=request.university_address,
        city=request.city,
        state=request.state,
        country=request.country,
        pincode=request.pincode
    )
    db.add(university_created)
    db.commit()
    return university_created.university_id

def get_university(university_id:str, db:Session):
    university = db.query(models.University).filter(models.University.university_id==university_id).first()
    if not university:
        raise HTTPException(status_code=404, detail="university not found")
    return {
            "university_id":university.university_id,
            "university_name":university.university_name,
            "university_address":university.university_address,
            "university_city": university.city,
            "university_state":university.state,
            

    }

def create_college(request:schemas.create_college,db:Session):
    university = db.query(models.University).filter(models.University.university_id == request.university_id).first()
    if not university:
        raise HTTPException(status_code=400, detail="Invalid university_id: university not found")
    college_created= models.College(
            college_id =generate_unique_id(),
            college_name=request.college_name,
            college_address=request.college_address,
            city=request.city,
            state=request.state,
            country=request.country,
            pincode=request.pincode,
            university_id=request.university_id
    )
    db.add(college_created)
    db.commit()
    return college_created.college_id

def get_college(college_id:str, db:Session):
    college= db.query(models.College).filter(models.College.college_id==college_id).first()
    if not college:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="college not found")
    return {
        "college_id":college.college_id,
        "college_name":college.college_name,
        "college_address":college.college_address
    }

def create_courses(request:schemas.create_courses,db:Session):
    college= db.query(models.College).filter(models.College.college_id==request.college_id).first()
    if not college:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="college not found")
    courses_create= models.Courses(
        course_id=generate_unique_id(),
        course_name=request.course_name,
        course_code=request.course_code,
        course_duration=request.course_duration,
        semester_count=request.semester_count,
        college_id=request.college_id
    )
    db.add(courses_create)
    db.commit()
    return courses_create.course_id

def get_courses(course_id:str,db:Session):
    courses= db.query(models.Courses).filter(models.Courses.course_id==course_id).first()
    if not courses:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="course not found")
    return {
        "course_id": courses.course_id,
        "course_name": courses.course_name,
        "course_duration":courses.course_duration
    }

def create_subjects(request:schemas.create_subjects,db:Session):
    courses= db.query(models.Courses).filter(models.Courses.course_id==request.course_id).first()
    if not courses:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="course not found")
    college= db.query(models.College).filter(models.College.college_id==request.college_id).first()
    if not college:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="college not found")
    subjects_created=models.Subjects(
        subject_id= generate_unique_id(),
        subject_name=request.subject_name,
        subject_code=request.subject_code,
        course_id=request.course_id,
        college_id=request.college_id
    )
    db.add(subjects_created)
    db.commit()
    return subjects_created.subject_id

def get_subject(subject_id:str,db:Session):
    subject= db.query(models.Subjects).filter(models.Subjects.subject_id==subject_id).first()
    if not subject:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="subject not found")
    return{
        "subject_name":subject.subject_name,
        "subject_id":subject.subject_id,
    }

def create_fee_structure(request:schemas.create_fee_structure,db:Session):

    college= db.query(models.College).filter(models.College.college_id==request.college_id).first()
    if not college:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="college not found")
 
    courses= db.query(models.Courses).filter(models.Courses.course_id==request.course_id).first()
    if not courses:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="course not found")
    fee_structure_created=models.FeeStructure(
        fee_id=generate_unique_id(),
        amount_per_semester=request.amount_per_semester,
        course_id=request.course_id,
        college_id=request.college_id
    )
    db.add(fee_structure_created)
    db.commit()
    return {"fee id":fee_structure_created.fee_id,"message":"fee structure is created successfully"}
  
def get_fee_structure(college_id:str, course_id:str, db:Session):
    fee= db.query(models.FeeStructure).filter(models.FeeStructure.college_id==college_id,models.FeeStructure.course_id==course_id).first()
    if not fee:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="fee structure not found")
    return{
        "course_id":fee.course_id,
        "college_id":fee.college_id,
        "fee_per_semester":fee.amount_per_semester,
        "total_fee":fee.total_amount
}

def create_user_college(request:schemas.create_user_college, db:Session):
    user = db.query(models.User).filter(models.User.user_id==request.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user does not exist")
    
    college = db.query(models.College).filter(models.College.college_id==request.college_id).first()
    if not college:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="college does not exist")
    
    create_user_college = models.User_college(
        user_college_id = generate_unique_id(),
        user_id = request.user_id,
        college_id = request.college_id
    )
    db.add(create_user_college)
    db.commit()
    return{
        "user_college_id":create_user_college.user_college_id,
        "user_id": create_user_college.user_id,
        "college_id":create_user_college.college_id
    }

def get_all_college_user(college_id:str,db:Session):
    college = db.query(models.User_college).filter(models.User_college.college_id== college_id).first()
    if not college :
     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="college does not exist")
    
    college_user =db.query(models.User_college).filter(models.User_college.college_id==college_id).all()
    return college_user

def calculate_total_fee(course_id: str, college_id: str, db: Session):
    # Get course duration
    course = db.query(models.Courses).filter(models.Courses.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Get fee per semester
    fee = db.query(models.FeeStructure).filter(
        models.FeeStructure.college_id == college_id,
        models.FeeStructure.course_id == course_id
    ).first()
    if not fee:
        raise HTTPException(status_code=404, detail="Fee structure not found")

    total_fee = course.semester_count * fee.amount_per_semester

    return {
        "course_id": course.course_id,
        "college_id": college_id,
        "duration_in_semesters": course.course_duration,
        "fee_per_semester": fee.amount_per_semester,
        "calculated_total_fee": total_fee
    }

def create_user_course(request:schemas.create_user_course,db:Session):
    user = db.query(models.User).filter(models.User.user_id==request.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user does not exist")
    
    course = db.query(models.Courses).filter(models.Courses.course_id == request.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    create_user_course = models.User_Course(
        user_course_id = generate_unique_id(),
        user_id = request.user_id,
        course_id = request.course_id
        )
    db.add(create_user_course)
    db.commit()

    return create_user_course.user_course_id

def create_roles(request:schemas.create_roles, db:Session):
    user = db.query(models.User).filter(models.User.user_id==request.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user does not exist")
    
    create_roles = models.Roles(
        role_id =generate_unique_id(),
        user_id = request.user_id,
        role_description = request.role_description
    )
    db.add(create_roles)
    db.commit()

    return create_roles.role_id
    

    
