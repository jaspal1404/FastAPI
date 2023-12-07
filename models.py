from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float



class Items(Base):
    __tablename__ = 'items'

    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    brand = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    driveup_allowed = Column(Boolean)
    shipping_allowed = Column(Boolean)
    store_pickup_allowed = Column(Boolean)
    store_id = Column(String)