from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///calendar_tasks.db')
Base = declarative_base()
# Base.metadata.create_all(engine)

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    task_name = Column(String, unique=False)
    start = Column(String, unique=False)
    end = Column(String, unique=False)
    priority = Column(String)

Session = sessionmaker(bind=engine)
session = Session()

def get_tasks_data():
    task_query = session.query(Task).all()
    tasks = []
    for obj in task_query:
        obj = obj.__dict__
        tasks.append(obj)
    return tasks

def add_task_data(task_data):
    """ Add a new task """
    new_user = Task(task_name=task_data['title'], start=task_data['start'], end = task_data['end'], priority = task_data['priority'])
    session.add(new_user)
    session.commit()

def edit_task(task_name, priority):
    """ Edit the priority of a Task"""
    user = session.query(Task).filter_by(task_name=task_name).first()
    user.priority = priority
    session.commit()

def shift_task():
    # shift task to next day if day ends
    pass