from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select
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

# session = Session(engine)

# new_user1 = User(name="John Doe", email="JohnDoe@email.com")
# new_user2 = User(name="Jane Doe", email="JaneDoe@email.com")

# new_product1 = Product(name="Laptop", price=1000)
# new_product2 = Product(name="Smartphone", price=500)
# new_product3 = Product(name="Tablet", price=300)

# new_order1 = Order(user_id=1, product_id=2, quantity=1)
# new_order2 = Order(user_id=2, product_id=1, quantity=5)
# new_order3 = Order(user_id=1, product_id=3, quantity=10)
# new_order4 = Order(user_id=2, product_id=3, quantity=3)

# session.add_all([new_user1, new_user2, new_product1, new_product2, new_product3])
# session.add_all([new_order1, new_order2, new_order3, new_order4])
# session.commit()

session = Session(engine)
user_query = select(User)
users = session.execute(user_query).scalars().all()
for user in users:
    print(user.name, user.email)

product_query = select(Product)
products = session.execute(product_query).scalars().all()
for product in products:
    print(product.name, product.price)

order_query = select(Order)
orders = session.execute(order_query).scalars().all()
for order in orders:
    print(f"User: {order.user.name}, Product: {order.product.name}, Quantity: {order.quantity}")
    
update_product_query = select(Product).where(Product.id == 1)
update_product = session.execute(update_product_query).scalars().first()
update_product.price = 900


# new_user3 = User(name="Delete me", email="DeleteMe@email.com")
# session.add(new_user3)
# session.commit()
# query = select(User).where(User.id == 3)
# user = session.execute(query).scalars().first()
# session.delete(user)

session.commit()
    
session.close()