from fastapi import APIRouter, Depends
from app.repository import user
from app import schemas,database
from sqlalchemy.orm import Session


router = APIRouter()
    
@router.post("/create/user")
def create_user(request:schemas.create_user,db:Session=Depends(database.get_db)):
    

    return user.create_user(request=request,db=db)

@router.get("/get/user/{user_id}")
def get_user(user_id:str,db:Session=Depends(database.get_db)):
    return user.get_user(user_id=user_id,db=db)

@router.post("/create/university")
def create_university(request:schemas.create_university,db:Session=Depends(database.get_db)):
    return user.create_university(request=request, db=db) 

@router.get("/get/university/{university_id}")
def get_university(university_id=str,db:Session=Depends(database.get_db)):
    return user.get_university(university_id=university_id,db=db)

@router.post("/post/college")
def create_college(request:schemas.create_college,db:Session=Depends(database.get_db)):
    return user.create_college(request=request,db=db)

@router.get("/get/college/{college_id}")
def get_college(college_id=str,db:Session=Depends(database.get_db)):
    return user.get_college(college_id=college_id,db=db)

@router.post("/course/post")
def create_course(request:schemas.create_courses,db:Session=Depends(database.get_db)):
    return user.create_courses(request=request,db=db)

@router.get("/course/get/{course_id}")
def courses_get(course_id=str,db:Session=Depends(database.get_db)):
    return user.get_courses(course_id=course_id,db=db)

@router.post("/post/subjects")
def subjects_created(request:schemas.create_subjects,db:Session=Depends(database.get_db)):
    return user.create_subjects(request=request,db=db)

@router.get("/get/subject/{subject_id}")
def subject_get(subject_id:str,db:Session=Depends(database.get_db)):
    return user.get_subject(subject_id=subject_id,db=db)

@router.post("/post/fee_structure")
def fee_structure_created(request:schemas.create_fee_structure,db:Session=Depends(database.get_db)):
    return user.create_fee_structure(request=request,db=db)

@router.get("/get/fee/{course_id}/{college_id}")
def fee_get(college_id:str, course_id:str, db:Session=Depends(database.get_db)):
    return user.get_fee_structure(course_id=course_id,college_id=college_id,db=db)

@router.post("/post/user-college")
def user_post(request:schemas.create_user_college, db:Session=Depends(database.get_db)):
    return user.create_user_college(request=request,db=db)

@router.get("/get/all/college/{college_id}")
def college_user_all_get(college_id:str,db:Session=Depends(database.get_db)):
    return  user.get_all_college_user(college_id=college_id,db=db)

@router.get("/get/total/fee/{college_id}/{course_id}", tags=["Fee"])
def calculate_total_fee(college_id: str, course_id: str, db: Session = Depends(database.get_db)):
    return user.calculate_total_fee(college_id=college_id, course_id=course_id, db=db)

@router.post("/post/user-course")
def user_course_post(request:schemas.create_user_course,db:Session = Depends(database.get_db)):
    return user.create_user_course(request=request,db=db)

@router.post("/post/roles")
def roles_post(request:schemas.create_roles, db:Session = Depends(database.get_db)):
    return user.create_roles(request=request,db=db)

