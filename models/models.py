from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from database.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)

    tasks = relationship("Task", back_populates="assigned_user")

class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True, index=True)
    description = Column(Text)
    assigned_to_user_id = Column(Integer, ForeignKey('users.user_id'))
    status = Column(String, default='assigned')  # assigned, done
    created_at = Column(DateTime, default=datetime.utcnow)
    done_at = Column(DateTime, nullable=True)
    document_file_id = Column(String, nullable=True)

    assigned_user = relationship("User", back_populates="tasks")
    reports = relationship("Report", back_populates="task")

class Report(Base):
    __tablename__ = 'reports'
    report_id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey('tasks.task_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    report_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    task = relationship("Task", back_populates="reports")