#coding:utf-8

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Base = db.Model

class Article(Base):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime)
