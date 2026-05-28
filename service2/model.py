from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from database import engine

Base = declarative_base()


class Employee(Base):
    __tablename__ = "Employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String ,index=True)
    age = Column(Integer,index=True)
    department = Column(String,index=True)
    salary = Column(Integer,index=True)


Base.metadata.create_all(bind=engine)
