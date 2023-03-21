DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `properties`;

CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    sale_type VARCHAR(50),
    sold_date TIMESTAMP,
    property_type VARCHAR(50),
    address VARCHAR(100),
    city VARCHAR(50),
    state_or_province VARCHAR(50),
    zip_or_postal_code VARCHAR(20),
    price FLOAT,
    beds INTEGER,
    baths FLOAT,
    location VARCHAR(50),
    square_feet FLOAT,
    lot_size FLOAT,
    year_built INTEGER,
    days_on_market INTEGER,
    price_per_square_feet FLOAT,
    hoa_per_month FLOAT,
    status VARCHAR(50),
    next_open_house_start_time VARCHAR(50),
    next_open_house_end_time VARCHAR(50),
    url VARCHAR(200),
    source VARCHAR(50),
    mls VARCHAR(50),
    favorite VARCHAR(10),
    interested VARCHAR(10),
    latitude FLOAT,
    longitude FLOAT
);
