import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, VARCHAR
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    username = Column(VARCHAR(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    favorites = relationship("Favorites", back_populates="User")

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    favorites = relationship("Favorites", back_populates="Planets")

class Characters(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    favorites = relationship("Favorites", back_populates="Characters")


class Starships(Base):
    __tablename__ = 'Starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    model = Column(String(250), nullable=False)
    favorites = relationship("Favorites", back_populates="Starships")


class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    user = relationship("User",back_populates="Favorites")
    planets_id = Column(Integer,ForeignKey("Planets.id"))
    planets = relationship("Planets", back_populates="Favorites")
    characters_id = Column(Integer, ForeignKey("Characters.id"))
    characters = relationship("Characters", back_populates="Favorites")
    starships_id = Column(Integer, ForeignKey("Starships.id"))
    starships = relationship("Starships", back_populates="Favorites")


render_er(Base, 'diagram.png')