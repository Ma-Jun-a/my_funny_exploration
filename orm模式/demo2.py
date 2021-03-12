from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()
class Student(base):
    __tablename__='student'
    s_id = Column(Integer,primary_key=True,autoincrement=True)
    s_name = Column(String(32),nullable=False,default='null')
    ctime = Column(DateTime,default=datetime.now)

class score(base):
    __tablename__ = 'score'
    id = Column(Integer,primary_key=True)
    s_id = Column(Integer,ForeignKey('student.s_id'),primary_key=True)
    c_id = Column(Integer,nullable=False)
    s_score = Column(Integer,nullable=False)


engine = create_engine("mysql+mysqlconnector://{user}:{pwd}@localhost:3306/{database}?charset=utf8".format(
    user='root',pwd='mysql',database='student_info3'),max_overflow=5)
base.metadata.create_all(engine)
# engine.create()
