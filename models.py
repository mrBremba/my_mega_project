from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///selfcult.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    password = Column(String(50))
    email = Column(String(120), unique=True)
    cur_goal_id = Column(Integer, ForeignKey('goal.id'))

    def __init__(self, name=None, password=None, email=None):
        self.name = name
        self.password = password
        self.email = email


class Goal(Base):
    __tablename__ = 'goal'
    id = Column(Integer, primary_key=True)
    goal_name = Column(String)


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    cur_goal_id = Column(Integer, ForeignKey('goal.id'))
    task = Column(String)    

class TaskHistory(Base):
    __tablename__ = 'task_history'
    id = Column(Integer, primary_key=True)
    task_state = Column(String(50))
    user_id = Column(Integer, ForeignKey('users.id'))
    cur_goal_id = Column(Integer, ForeignKey('goal.id'))
    created = Column(DateTime)
    updated = Column(DateTime)

    def __init__(self, task_state=None, user_id=None, cur_goal_id=None):
        self.task_state = task_state
        self.user_id = user_id
        self.cur_goal_id = cur_goal_id

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)