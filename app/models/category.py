from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship

from database import Base


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String,nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    products = relationship("Product", back_populates="category")