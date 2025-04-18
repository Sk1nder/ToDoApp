from flask_login import UserMixin
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, DateTime, Boolean

from ToDoAPP import db


class Task(db.Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="tasks")
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text)
    deadline: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    startDate: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    endDate: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    status: Mapped[bool] = mapped_column(Boolean, default=False)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    tasks = relationship("Task", back_populates="author")




