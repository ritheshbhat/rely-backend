from sqlalchemy import Column, Integer, String, Float, DateTime, func

from src.rely import db
from test.rely import db


# 62a1312f-f59e-47cf-8d2f-159e2a68eaf7 -> rithesh
# e902ac39-69d6-4fda-9f29-689d1820c457 -> soham


class Property(db.Model):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sale_type = Column(String(50))
    sold_date = Column(DateTime)
    property_type = Column(String(50))
    address = Column(String(100))
    city = Column(String(50))
    state_or_province = Column(String(50))
    zip_or_postal_code = Column(String(20))
    price = Column(Float)
    beds = Column(Integer)
    baths = Column(Float)
    location = Column(String(50))
    square_feet = Column(Float)
    lot_size = Column(Float)
    year_built = Column(Integer)
    days_on_market = Column(Integer)
    price_per_square_feet = Column(Float)
    hoa_per_month = Column(Float)
    status = Column(String(50))
    next_open_house_start_time = Column(String(50))
    next_open_house_end_time = Column(String(50))
    url = Column(String(200))
    source = Column(String(50))
    mls = Column(String(50))
    favorite = Column(String(10))
    interested = Column(String(10))
    latitude = Column(Float)
    longitude = Column(Float)


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    mobile_number = Column(String(20))
    address = Column(String(100))
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    last_updated_on = Column(DateTime(timezone=True), onupdate=func.now())

def setup_database():
    db.drop_all()
    db.create_all()
    property = Property(sale_type='For Sale', property_type='Single Family', address='123 Main St', city='Anytown',
                        state_or_province='CA', zip_or_postal_code='12345', price=1000000, beds=3, baths=2.5,
                        location='Downtown', square_feet=2000, lot_size=0.25, days_on_market=7,
                        price_per_square_feet=500, status='Active', url='https://www.example.com/property/123',
                        source='MLS', mls='123456', favorite='No', interested='Yes')
    db.session.add(property)
    db.session.commit()
z