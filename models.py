from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Institute(Base):
    __tablename__ = "institute"

    institute_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    institute_name = Column(String(100), unique=True, nullable=False)

class Course(Base):
    __tablename__ = "course"

    course_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    institute_id = Column(Integer, ForeignKey('institute.institute_id'), nullable=False)
    course_name = Column(String(100), nullable=False)

class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    institute_id = Column(Integer, ForeignKey('institute.institute_id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)
    student_name = Column(String(100), nullable=False)
    joining_date = Column(Date, nullable=False)
