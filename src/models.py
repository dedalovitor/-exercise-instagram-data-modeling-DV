import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    active = Column(Boolean, default=True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    content= Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id')) #representa el ForeignKey, diciéndole de dónde va a agarrar los datos, de la tabla user columna id
    user = relationship(User) # representa la relación entre tablas

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content= Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id')) #representa el ForeignKey, diciéndole de dónde va a agarrar los datos, de la tabla user columna id
    user = relationship(User) # representa la relación entre tablas
    post_id = Column(Integer, ForeignKey('post.id')) #representa el ForeignKey, diciéndole de dónde va a agarrar los datos, de la tabla user columna id
    post = relationship(Post) # representa y relación entre tablas

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id')) #representa el ForeignKey, diciéndole de dónde va a agarrar los datos, de la tabla user columna id
    post = relationship(Post) # representa y relación entre tablas

class Follower (Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True) # el id siempre es necesario
    user_from_id= Column(Integer, ForeignKey('user.id'))  #quien da el follow
    user_to_id= Column(Integer, ForeignKey('user.id'))  #a quien le llega el follow
    user = relationship(User) # representa y relación entre tablas
    

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
