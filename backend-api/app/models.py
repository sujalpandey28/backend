from datetime import datetime, timezone
from enum import Enum
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Date,
    ForeignKey,
    Integer,
    String,
    func,
    Float,
    Text,
    Time,
    Enum as SQLAEnum,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from .database import Base

class User_roles(str,Enum):
    student = "students"
    teacher = "teacher"

class User(Base):
    __tablename__= "user"
    user_id= Column(String(16),primary_key=True,unique=True)
    name=Column(String(64),nullable=True)
    email=Column(String(64),nullable=False,unique=True)
    password=Column(String(64),nullable=False)
    mobile=Column(String(16),nullable=False,unique=True)

    created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

class Roles(Base):
    __tablename__="roles"
    role_id= Column(String(16), primary_key=True,unique=True)
    user_id=  Column(String(16),ForeignKey("user.user_id"),nullable=False)
    role_description= Column(SQLAEnum(User_roles),index=True)

class College(Base):
    __tablename__="college"
    college_id =Column(String(16), primary_key=True,unique=True)
    college_name= Column(String(16),nullable=False)
    college_address=Column(String(64),nullable=False)
    city= Column(String(16),nullable=False)
    state= Column(String(16),nullable=False)
    country=Column(String(16),nullable=False)
    pincode= Column(String(16),nullable=True)
    university_id=Column(String(16),ForeignKey("university.university_id"), nullable=False)

class University(Base):
    __tablename__="university"
    university_id =Column(String(16), primary_key=True,unique=True)
    university_name= Column(String(16),nullable=False)
    university_address=Column(String(64),nullable=False)
    city= Column(String(16),nullable=False)
    state= Column(String(16),nullable=False)
    country=Column(String(16),nullable=False)
    pincode= Column(String(16),nullable=True)

class Courses(Base):
    __tablename__= "courses"
    course_id=Column(String(16), primary_key=True,unique=True)
    course_name=Column(String(16),nullable=False)
    course_code= Column(String(16),nullable=False)
    course_duration=Column(Integer,nullable=False)#in no.of years
    semester_count= Column(Integer,nullable=False)
    college_id= Column(String(16),ForeignKey("college.college_id"),nullable=False)

class Subjects(Base):
    __tablename__= "subject"
    subject_id=Column(String(16), primary_key=True,unique=True)
    subject_name=Column(String(16),nullable=False)
    subject_code=Column(String(16),nullable=False)
    course_id=Column(String(16),ForeignKey("courses.course_id"),nullable=False)
    college_id=Column(String(16),ForeignKey("college.college_id"),nullable=False)

class FeeStructure(Base):
    __tablename__="fee_structure"
    fee_id=Column(String(16), primary_key=True,unique=True)
    amount_per_semester =Column(Integer,nullable=False)#per semester
    course_id= Column (String(16), ForeignKey("courses.course_id"),nullable=False)
    college_id =Column(String(16), ForeignKey("college.college_id"),nullable=False)
    total_amount=Column(Integer,nullable=True)
    
class User_college(Base):
    __tablename__="user_college"
    user_college_id=Column(String(16), primary_key=True,unique=True)
    user_id= Column(String(16),ForeignKey("user.user_id"),nullable=False)
    college_id=Column(String(16),ForeignKey("college.college_id"),nullable=False)

class User_Course(Base):
    __tablename__="user_courses"
    user_course_id= Column(String(16), primary_key=True,unique=True)
    user_id=Column(String(16),ForeignKey("user.user_id"),nullable=False)
    course_id= Column(String(16),ForeignKey("courses.course_id"),nullable=False)

class User_subject(Base):
    __tablename__="user_subject"
    user_subject_id=Column(String(16), primary_key=True,unique=True)
    user_id= Column(String(16),ForeignKey("user.user_id"),nullable=False)
    subject_id=Column(String(16),ForeignKey("subject.subject_id"),nullable=False)







    




    