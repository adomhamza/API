from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text, true
from sqlalchemy.sql.sqltypes import TIMESTAMP


from .database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=true), nullable=False,
                        server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=true),
                        nullable=False, server_default=text('now()'))
    role_id = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)


class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    category_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    inventory = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    sold_count = Column(Integer, nullable=False)
    # image = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=true),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=true),
                        nullable=False, server_default=text('now()'))


class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True, nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    payment_method_id = Column(Integer, nullable=False)
    payment_status = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=true),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=true),
                        nullable=False, server_default=text('now()'))
