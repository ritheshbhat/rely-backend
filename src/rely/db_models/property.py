from sqlite3 import Date

from sqlalchemy import Column, Integer, String, Float, DateTime


from src.rely import db


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
