# Write your code here

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from datetime import timedelta
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, )
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
while True:
    print("1) Today's tasks")
    print("2) Week's tasks")
    print('3) All tasks')
    print('4) Missed tasks')
    print('5) Add task')
    print('6) Delete task')
    print('0) Exit')
    user_choice = input()
    print()
    if user_choice == '0':
        print('Bye!')
        break
    elif user_choice == '1':
        today = datetime.now()
        month_now = today.strftime("%b")
        day_now = today.day
        print('Today {} {}:'.format(day_now, month_now))
        rows = session.query(Task).filter(Task.deadline == today.date()).all()
        if len(rows) == 0:
            print('Nothing to do!')
        else:
            for i in range(len(rows)):
                print("{}. {}".format(i+1, rows[i].task))
    elif user_choice == '2':
        today = datetime.now()
        for i in range(7):
            filter_day = today + timedelta(days=i)
            rows = session.query(Task).filter(filter_day.date() == Task.deadline).all()
            print('{} {} {}:'.format(filter_day.strftime("%A"), filter_day.strftime("%-d"), filter_day.strftime("%b")))
            if len(rows) == 0:
                print('Nothing to do!')
            else:
                for j in range(len(rows)):
                    print("{}. {}".format(j + 1, rows[j].task))
            print()
    elif user_choice == '3':
        print('All tasks:')
        rows = session.query(Task).order_by(Task.deadline).all()
        if len(rows) == 0:
            print('Nothing to do!')
        else:
            for i in range(len(rows)):
                print("{}. {}. {} {}".format(i+1, rows[i].task, rows[i].deadline.strftime("%-d"), rows[i].deadline.strftime("%b")))
    elif user_choice == '4':
        print('Missed tasks:')
        rows = session.query(Task).filter(datetime.now() > Task.deadline).all()
        if len(rows) == 0:
            print('Nothing is missed!!')
        else:
            for i in range(len(rows)):
                print("{}. {}".format(i + 1, rows[i].task))
    elif user_choice == '5':
        print('Enter task')
        task_description = input()
        print('Enter deadline')
        date_str = input()
        deadline = datetime.strptime(date_str, '%Y-%m-%d')
        new_row = Task(task=task_description, deadline=deadline)
        session.add(new_row)
        session.commit()
        print('The task has been added!')
    elif user_choice == '6':
        print('Choose the number of the task you want to delete:')
        rows = session.query(Task).all()
        if len(rows) == 0:
            print('Nothing to delete')
        else:
            for i in range(len(rows)):
                print("{}. {}. {} {}".format(i+1, rows[i].task, rows[i].deadline.strftime("%-d"), rows[i].deadline.strftime("%b")))
            delete_input = int(input())
            session.delete(rows[delete_input-1])
            session.commit()
            print('The task has been deleted!')
    print()
