from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Teacher(Base):
    __tablename__ = "Teacher"
    id = Column(Integer, primary_key=True)
    first_last_name = Column(String)
    kafedra = Column(String)
    degree = Column(String)
    job_title = Column(String)
    
    # 1->N
    participance = relationship("Participance", back_populates="Teacher")


class Classes(Base):
    __tablename__ = "Classes"
    id = Column(Integer, primary_key=True)
    time = Column(Date)
    group = Column(Integer)
    room = Column(Integer)
    date = Column(Date)
    class_name = Column(String)

    # N->1
    teacher_id = Column(ForeignKey("Teacher.id", ondelete="CASCADE"))
    teacher = relationship("Teacher", back_populates="participance", cascade="all,delete")

    # N->1
    lesson_id = Column(ForeignKey("lesson.id", ondelete="CASCADE"))
    lesson = relationship("Lesson", back_populates="participance", cascade="all,delete")




class Lesson(Base):
    __tablename__ = "Lesson"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    count_of_times = Column(Integer)
    how_to_check = Column(String)
    obligation = Column(String)
    

    # 1->N
    participance = relationship("Participance", back_populates="Lesson")