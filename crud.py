from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Teacher, Classes, Lesson
from scheme import TeacherCreate, TeacherResponse, ClassesCreate, ClassesResponse, LessonCreate, LessonResponse
from creating_db import DATABASE_URL as db_url
import uvicorn
from typing import List

app = FastAPI()
DATABASE_URL = db_url
db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hi"}

@app.post("/teachers/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = Teacher(**teacher.model_dump())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@app.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="teacher not found")
    return db_teacher

@app.get("/teachers/", response_model=List[TeacherResponse])
def get_all_teachers(page: int = 1, page_size: int = 20, db: Session = Depends(get_db)):
    
    offset = (page - 1) * page_size
    teachers = db.query(Teacher).offset(offset).limit(page_size).all()
    return teachers

@app.put("/teachers/{teacher_id}", response_model=TeacherResponse)
def update_teacher(teacher_id: int, updated_teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="teacher not found")

    for field, value in updated_teacher.model_dump().items():
        setattr(db_teacher, field, value)

    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@app.delete("/teachers/{teacher_id}", response_model=TeacherResponse)
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="teacher not found")

    db.delete(db_teacher)
    db.commit()
    return db_teacher





@app.post("/lessons/", response_model=LessonResponse)
def create_lesson(lesson: LessonCreate, db: Session = Depends(get_db)):
    db_lesson = lesson(**lesson.model_dump())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

@app.get("/lessons/{lesson_id}", response_model=LessonResponse)
def read_lesson(lesson_id: int, db: Session = Depends(get_db)):
    db_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if db_lesson is None:
        raise HTTPException(status_code=404, detail="lesson not found")
    return db_lesson

@app.get("/lessons/", response_model=List[LessonResponse])
def get_all_lessons(page: int = 1, page_size: int = 20, db: Session = Depends(get_db)):

    offset = (page - 1) * page_size
    lessons = db.query(Lesson).offset(offset).limit(page_size).all()
    return lessons

@app.put("/lessons/{lesson_id}", response_model=LessonResponse)
def update_lesson(lesson_id: int, updated_lesson: LessonCreate, db: Session = Depends(get_db)):
    db_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if db_lesson is None:
        raise HTTPException(status_code=404, detail="lesson not found")

    for field, value in updated_lesson.model_dump().items():
        setattr(db_lesson, field, value)

    db.commit()
    db.refresh(db_lesson)
    return db_lesson

@app.delete("/lessons/{lesson_id}", response_model=LessonResponse)
def delete_lesson(lesson_id: int, db: Session = Depends(get_db)):
    db_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if db_lesson is None:
        raise HTTPException(status_code=404, detail="lesson not found")

    db.delete(db_lesson)
    db.commit()
    return db_lesson





@app.post("/classess/", response_model=ClassesResponse)
def create_classes(classes: ClassesCreate, db: Session = Depends(get_db)):
    db_classes = Classes(**classes.model_dump())
    db.add(db_classes)
    db.commit()
    db.refresh(db_classes)
    return db_classes

@app.get("/classess/{classes_id}", response_model=ClassesResponse)
def read_classes(classes_id: int, db: Session = Depends(get_db)):
    db_classes = db.query(Classes).filter(Classes.id == classes_id).first()
    if db_classes is None:
        raise HTTPException(status_code=404, detail="classes not found")
    return db_classes

@app.get("/classess/", response_model=List[ClassesResponse])
def get_all_classess(page: int = 1, page_size: int = 20, db: Session = Depends(get_db)):

    offset = (page - 1) * page_size

    # Can navigate through pages adding ?page={the page number} to the url
    classess = db.query(Classes).offset(offset).limit(page_size).all()
    return classess

@app.put("/classess/{classes_id}", response_model=ClassesResponse)
def update_classes(classes_id: int, updated_classes: ClassesCreate, db: Session = Depends(get_db)):
    db_classes = db.query(Classes).filter(Classes.id == classes_id).first()
    if db_classes is None:
        raise HTTPException(status_code=404, detail="classes not found")

    for field, value in updated_classes.model_dump().items():
        setattr(db_classes, field, value)

    db.commit()
    db.refresh(db_classes)
    return db_classes

@app.delete("/classess/{classes_id}", response_model=ClassesResponse)
def delete_classes(classes_id: int, db: Session = Depends(get_db)):
    db_classes = db.query(Classes).filter(Classes.id == classes_id).first()
    if db_classes is None:
        raise HTTPException(status_code=404, detail="classes not found")

    db.delete(db_classes)
    db.commit()
    return db_classes
uvicorn.run(app, host="127.0.0.1", port=8000)
