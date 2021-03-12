from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, and_, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()
class student(base):
    __tablename__ = 'student'
    # id = Column(Integer,primary_key=True,)
    s_id = Column(Integer,nullable=False,primary_key=True)
    s_name = Column(String(32),nullable=False)
    s_birth = Column(String(8),nullable=False)
    s_sex = Column(String(10),nullable=False)

class score(base):
    __tablename__ = 'score'
    id = Column(Integer,primary_key=True)
    # s_id = Column(Integer,ForeignKey('student.s_id'),primary_key=True)
    c_id = Column(Integer,nullable=False)
    s_score = Column(Integer,nullable=False)

class course(base):
    __tablename__ = 'course'
    id = Column(Integer,primary_key=True)
    # c_id = Column(Integer,ForeignKey('score.c_id'))
    c_name = Column(String(32),nullable=False)
    t_id = Column(Integer,nullable=False)

class teacher(base):
    __tablename__ = 'teacher'
    id = Column(Integer,primary_key=True)
    # t_id = Column(Integer,ForeignKey('course.t_id'))
    t_name = Column(String(32),nullable=False)
    __table_args__ = ()

def create_db():
    engine = create_engine('mysql+mysqlconnector://root:mysql@127.0.0.1:3306/student_info2?charset=utf8',max_overflow=5)
    base.metadata.create_all(engine)
def drop_db():
    engine = create_engine('mysql+mysqlconnector://root:mysql@127.0.0.1:3306/student_info2?charset=utf8',
                           max_overflow=5)
    base.metadata.drop_all(engine)
# create_db()
engine = create_engine('mysql+mysqlconnector://root:mysql@127.0.0.1:3306/student_info2?charset=utf8',max_overflow=5)

session = sessionmaker()
session = session(bind=engine)

# obj = teacher(t_name='王老师')
objs = [
    # student(s_name='赵雷',s_birth='1990-01-01',s_sex='male'),
    # student(s_name='赵er', s_birth='1990-02-01', s_sex='female'),
    # student(s_name='赵san', s_birth='1995-01-01', s_sex='female'),
    student(s_name='赵雷',s_birth='1990',s_sex='male'),
    student(s_name='赵er', s_birth='1990', s_sex='female'),
    student(s_name='赵san', s_birth='1995', s_sex='female'),
]
# 增删改查
result = session.query(student.s_name,student.s_birth).filter(student.s_id=='2')
# session.add_all(objs)
session.query(student.s_birth).filter(student.s_id=='03').update({'s_name':'lisi'})
session.query(student.s_birth).filter(student.s_id<'03').update({student.s_name:student.s_name+'{}x'.format(1)},synchronize_session=False)
session.query(student.s_birth).filter(student.s_id=='03').update({student.s_name:student.s_name+ 1},synchronize_session='evaluate')
# session.query(student.s_birth).filter(student.s_id=='03').delete()
#  条件查询
session.query(student.s_name).filter(and_(student.s_id>'3',student.s_name=='张三'))
session.query(student.s_name).filter(student.s_name.like('%张'))
session.query(student.s_name).filter(student.s_name.like('%张')).order_by(student.s_id.desc())
session.query(func.max(student.s_id)).group_by().having()
session.query(student.s_id).join(score,isouter=True).filter(student.s_id==score.id)
session.query(student.s_id,session.query().filter().as_scalar())
# 谁有foreignkey relation就写到那里面
# *** = relationship('表一',backref=表二'**.oo')

session.commit()
session.close()

