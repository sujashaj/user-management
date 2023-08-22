import hashlib
from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'

username = Column(String, primary_key=True)
email = Column(String, unique=True)
password = Column(String)
is_verified = Column(Boolean, default=False)

class User:
 def __init__(self, username, email, password):
    self.username = username
    self.email = email



