from datetime import date
import os
from sqlalchemy import Column, ForeignKey, String, create_engine, Date, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Table to support the Many-to-Many relationship
'''

Show = db.Table('show',
    Column('movie_id', Integer, db.ForeignKey('movies.id'), primary_key=True),
    Column('actor_id', Integer, db.ForeignKey('actors.id'), primary_key=True)
)

'''
Movie
Attributes: Title and Release Date
'''
class Movie(db.Model):  
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String(120))
  release_date = Column(Date, default=date.today)
  actors = db.relationship('Actor', backref='show', lazy=True)


  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date

  def insert(self):
      db.session.add(self)
      db.session.commit()

  def update(self):
      db.session.commit()

  def delete(self):
      db.session.delete(self)
      db.session.commit()

  def format(self):
      return {
          'id': self.id,
          'title': self.title,
          'releasedate': self.release_date
      }

  def __repr__(self):
      return f'Movie (id= {self.id}, title= {self.title}, release_date= {self.release_date})'

'''
Actor
Attributes: Name, Age and Gender
'''
class Actor(db.Model):  
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String(120))
  age = Column(Date, default=date.today)
  gender = Column(String(50))

  def __init__(self, title, release_date):
    self.title = title.title
    self.release_date = release_date

  def insert(self):
      db.session.add(self)
      db.session.commit()

  def update(self):
      db.session.commit()

  def delete(self):
      db.session.delete(self)
      db.session.commit()

  def format(self):
      return {
          'id': self.id,
          'name': self.name,
          'age': self.age,
          'gender': self.gender
      }

  def __repr__(self):
      return f'Actor(id= {self.id}, name= {self.name}, age= {self.age}, gender= {self.gender})'

# '''
# Person
# Have title and release year
# '''
# class Person(db.Model):  
#   __tablename__ = 'People'

#   id = Column(db.Integer, primary_key=True)
#   name = Column(String)
#   catchphrase = Column(String)

#   def __init__(self, name, catchphrase=""):
#     self.name = name
#     self.catchphrase = catchphrase

#   def format(self):
#     return {
#       'id': self.id,
#       'name': self.name,
#       'catchphrase': self.catchphrase}