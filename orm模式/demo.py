from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
class student(base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True,)
    s_id = Column(Integer,nullable=False)
    s_name = Column(String(32),nullable=False)
    s_birth = Column(String(8),nullable=False)
    s_sex = Column(String(10),nullable=False)

class score(base):
    __tablename__ = 'score'
    id = Column(Integer,primary_key=True)
    s_id = Column(Integer,ForeignKey('student.s_id'),primary_key=True)
    c_id = Column(Integer,nullable=False)
    s_score = Column(Integer,nullable=False)

class course(base):
    __tablename__ = 'course'
    id = Column(Integer,primary_key=True)
    c_id = Column(Integer,ForeignKey('score.c_id'))
    c_name = Column(String(32),nullable=False)
    t_id = Column(Integer,nullable=False)

class teacher(base):
    __tablename__ = 'teacher'
    id = Column(Integer,primary_key=True)
    t_id = Column(Integer,ForeignKey('course.t_id'))
    t_name = Column(String(32),nullable=False)
    __table_args__ = ()


engine = create_engine('mysql+mysqlconnector://root:mysql@127.0.0.1:3306/student_info2?charset=utf8',max_overflow=5)
base.metadata.create_all(engine)
