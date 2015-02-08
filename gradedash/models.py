from sqlalchemy import Column, Integer, String
from gradedash.database import Base

class Student(Base):
	__tablename__ = 'students'
	id = Column(Integer, primary_key=True)
	first_name = Column(String(45))
	last_name = Column(String(45))
	email = Column(String(128))

