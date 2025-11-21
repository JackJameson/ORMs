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

    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
    
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)

    user = relationship("User", back_populates="orders")
    product = relationship("Product")
    
Base.metadata.create_all(engine)

session = Session(engine)

# new_user1 = User(name="John Doe", email="JohnDoe@email.com")
# new_user2 = User(name="Jane Doe", email="JaneDoe@email.com")

new_product1 = Product(name="Laptop", price=1000)
new_product2 = Product(name="Smartphone", price=500)
new_product3 = Product(name="Tablet", price=300)

session.commit()