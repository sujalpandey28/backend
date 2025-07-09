from typing import Optional
from pydantic import BaseModel
from app import models


class create_user(BaseModel):
    name:str
    email:str
    password:str
    mobile:str

class create_university(BaseModel):
    university_name:str
    university_address:str
    city:str
    state:str
    country:str
    pincode:str

class create_college(BaseModel):
    college_name:str
    college_address:str
    city:str
    state:str
    country:str
    pincode:Optional[str]= None
    university_id:str

class create_courses(BaseModel):
    course_name:str
    course_code:str
    course_duration:int
    semester_count:int
    college_id:str

class create_subjects(BaseModel):
    subject_name:str
    subject_code:str
    course_id:str
    college_id:str

class create_fee_structure(BaseModel):
    amount_per_semester:int
    course_id:str
    college_id:str

class create_user_college(BaseModel):
    user_id:str
    college_id:str


class create_user_course(BaseModel):
    user_id:str
    course_id:str

class create_roles(BaseModel):
    user_id:str
    role_description:models.User_roles