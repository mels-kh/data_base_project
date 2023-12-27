from pydantic import BaseModel
from datetime import date

from pydantic import BaseModel

class ClassesCreate(BaseModel):
    time : date
    group : int
    room : int
    date : date
    class_name : str
    teacher_id : int
    lesson_id : int
class ClassesResponse(ClassesCreate):
    id: int

class TeacherCreate(BaseModel):
    first_last_name : str
    kafedra : str
    degree : str
    job_title : str

class TeacherResponse(TeacherCreate):
    id: int

class LessonCreate(BaseModel):
    name : str
    count_of_times : int
    how_to_check : str
    obligation : str
    

class LessonResponse(LessonCreate):
    id: int


