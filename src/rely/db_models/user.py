from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from src.rely import db


# Create a database engine

# Define a User class that inherits from Base
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    mobile_number = Column(String(20))
    address = Column(String(100))
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    last_updated_on = Column(DateTime(timezone=True), onupdate=func.now())


