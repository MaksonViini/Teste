from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql.schema import Column
from database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)
    sex = Column(String(255))
    # graduate = Column(Boolean)
    # email = Column(String(255))
    # password = Column(String(255))
