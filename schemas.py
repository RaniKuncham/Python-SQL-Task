from pydantic import BaseModel
from datetime import date
from typing import Optional

class InstituteCreate(BaseModel):
    institute_name: str

class CourseCreate(BaseModel):
    institute_id: int
    course_name: str

class StudentCreate(BaseModel):
    institute_id: int
    course_id: int
    student_name: str
    joining_date: date

class SearchResult(BaseModel):
    institute_name: str
    course_name: str
    student_name: str
    joining_date: date
