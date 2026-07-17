from database import Base
from sqlalchemy import column,Integer,String,Boolean,Float

class Todos(Base):
    __tablename__ = 'todos'
    id = column(Integer, primary_key = True)
    title = column(String)
    description = column(String)
    priority = column(Integer)
    completed = column(Boolean,default = False)