from sqlalchemy import Column,Integer,String,Boolean,VARCHAR,ForeignKey
from database import Base

class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer,primary_key=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean,default=False)
    owner_id = Column(Integer,ForeignKey("users.id"))
