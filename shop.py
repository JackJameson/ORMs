from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Session, relationship, DeclarativeBase

engine = create_engine('mysql+mysqlconnector://root:password@localhost/shop')

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    # One-to-Many: User -> List of Order objects
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
    
Base.metadata.create_all(engine)

session = Session(engine)