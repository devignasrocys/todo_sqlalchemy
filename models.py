from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/database.db')
Base = declarative_base()

class User(Base):
    __tablename__= "user"
    id = Column(Integer, primary_key=True)
    username = Column("username", String)
    password = Column("password", String)
    todos = relationship("Todo", back_populates="user")

class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    todo = Column("todo", String)
    status = Column("status", String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="todos")

if __name__ == "__main__":
    Base.metadata.create_all(engine)