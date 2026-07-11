from sqlalchemy import Column  , Integer , ForeignKey , String , Text
from db import Base , engine


class User(Base):
    __tablename__="users"
    id=Column(Integer , primary_key=True )
    email=Column(String(100) , unique=True)
    password=Column(String(100))

class Report(Base):
    __tablename__="reports"
    id=Column(Integer , primary_key=True)
    user_id=Column(Integer , ForeignKey("users.id"))
    resume_text=Column(Text)
    result=Column(Text)

Base.metadata.create_all(bind=engine)