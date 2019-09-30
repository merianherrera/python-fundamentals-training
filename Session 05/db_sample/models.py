from db_sample.db import Base
from sqlalchemy import Column, Integer, Text, String


class Category(Base):
    __tablename__ = 'Categories'
    CategoryID = Column(Integer, primary_key=True)
    CategoryName = Column(Text, unique=True, nullable=False)
    Description = Column(Text, unique=False, nullable=False)

    def __repr__(self):
        return f'{self.CategoryName}: {self.Description}'


class Customers(Base):
    __tablename__ = 'Customers'
    CustomerID = Column(String, primary_key=True)
    CompanyName = Column(Text, nullable=False)
    ContactName = Column(Text, nullable=False)
    ContactTitle = Column(Text, nullable=True)
    Address = Column(Text, nullable=True)
    City = Column(Text, nullable=True)
    Region = Column(Text, nullable=True)
    PostalCode = Column(Text, nullable=True)
    Country = Column(Text, nullable=True)
    Phone = Column(Text, nullable=True)
    Fax = Column(Text, nullable=True)
