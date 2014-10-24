

DROP TABLE IF EXISTS customer;
CREATE TABLE customer (
  cust_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  fname VARCHAR(30),
  lname VARCHAR(30),
  password VARCHAR(30),
  cust_email VARCHAR(50),
  phone_number BIGINT,
  PRIMARY KEY(cust_id)
);

DROP TABLE IF EXISTS properties;
CREATE TABLE properties (
  property_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  property_type VARCHAR(30),
  bedrooms SMALLINT,
  bathrooms SMALLINT,
  sqft SMALLINT,
  lotsize SMALLINT,
  MINprice BIGINT,
  MAXprice BIGINT,
  address VARCHAR(200),
  city VARCHAR(30),
  zipcode SMALLINT,
  user SMALLINT,
  PRIMARY KEY(property_id)
);

DROP TABLE IF EXISTS offers;
CREATE TABLE offers (
  offer_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  cust_id SMALLINT,
  property_id SMALLINT,
  bid BIGINT,
  amtsold BIGINT,
  decision SMALLINT,
  PRIMARY KEY(offer_id)

);


INSERT INTO customer (fname, lname, phone_number, password, cust_email) VALUES ('Jane', 'Doe', 3476146271, 'cookie', 'janedoe@gmail.com');
INSERT INTO customer (fname, lname, phone_number, password, cust_email) VALUES ('Harry', 'Smith', 6503288181, 'cookie', 'harrysmith@gmail.com');
INSERT INTO customer (fname, lname, phone_number, password, cust_email) VALUES ('Louise', 'Johnson', 1172531868, 'cookie', 'louisejohnson@gmail.com');
INSERT INTO customer (fname, lname, phone_number, password, cust_email) VALUES ('Robin', 'Jean', 2123544747, 'cookie', 'robinjean@gmail.com');
INSERT INTO customer (fname, lname, phone_number, password, cust_email) VALUES ('Vanessa', 'Jeffrey', 3476146271, 'cookie', 'vjeffrey@gmail.com');
INSERT INTO customer (fname, lname, phone_number, password, cust_email) VALUES ('Pat', 'Humphries', 3476146271, 'cookie', 'phumphries@gmail.com');
INSERT INTO customer (fname, lname, phone_number, password, cust_email) VALUES ('Eliza', 'Kane', 3476146271, 'cookie', 'elizakane@gmail.com');
INSERT INTO customer (fname, lname, phone_number, password, cust_email) VALUES ('John', 'Doe', 3476146271, 'cookie', 'johndoe@gmail.com');
INSERT INTO customer (fname, lname, phone_number, password, cust_email) VALUES ('Kerry', 'Williams', 3476146271, 'cookie', 'kerrywilliams@gmail.com');
INSERT INTO customer (fname, lname, phone_number, password, cust_email) VALUES ('Paul', 'Wright', 3476146271, 'cookie', 'paulwright@gmail.com');


INSERT INTO properties (property_type, bedrooms, bathrooms, sqft, lotsize, MINprice, MAXprice, address, city, zipcode, user) VALUES ('Apartment', 1, 1, 900, 900, 27000, 30000, '814 Calamansi Drive', 'Makati', 10022, 1);
INSERT INTO properties (property_type, bedrooms, bathrooms, sqft, lotsize, MINprice, MAXprice, address, city, zipcode, user) VALUES ('Apartment', 2, 1, 1500, 1500, 30000, 39990, '270 Berlin Street', 'Makati', 10022, 2);
INSERT INTO properties (property_type, bedrooms, bathrooms, sqft, lotsize, MINprice, MAXprice, address, city, zipcode, user) VALUES ('House', 3, 2, 100, 2500, 30000, 45000, '18 Melbourne Steet', 'Makati', 10022, 3);
INSERT INTO properties (property_type, bedrooms, bathrooms, sqft, lotsize, MINprice, MAXprice, address, city, zipcode, user) VALUES ('House', 4, 2, 100, 2500, 35000, 60000, '91 Tamarind Street', 'Dasmarinas', 10011, 4);
INSERT INTO properties (property_type, bedrooms, bathrooms, sqft, lotsize, MINprice, MAXprice, address, city, zipcode, user) VALUES ('House', 6, 4, 100, 2000, 15999, 23500, '99 Madrid Street', 'Dasmarinas', 10011, 5);
INSERT INTO properties (property_type, bedrooms, bathrooms, sqft, lotsize, MINprice, MAXprice, address, city, zipcode, user) VALUES ('Apartment', 3, 4, 1000, 1000, 69000, 88000, '8 Mahogany Street', 'Dasmarinas', 10011, 6);
INSERT INTO properties (property_type, bedrooms, bathrooms, sqft, lotsize, MINprice, MAXprice, address, city, zipcode, user) VALUES ('House', 4, 3, 100, 2000, 235000, 335000, '8 Washington Street', 'Merville', 10003, 7);
INSERT INTO properties (property_type, bedrooms, bathrooms, sqft, lotsize, MINprice, MAXprice, address, city, zipcode, user) VALUES ('House', 6, 5, 100, 1999, 115000, 120000, '12 Lugang Street', 'Forbes', 10025, 8);
INSERT INTO properties (property_type, bedrooms, bathrooms, sqft, lotsize, MINprice, MAXprice, address, city, zipcode, user) VALUES ('Apartment', 2, 1, 850, 850, 40000, 50000, '4 Dalandan Street', 'Forbes', 10025, 9);
INSERT INTO properties (property_type, bedrooms, bathrooms, sqft, lotsize, MINprice, MAXprice, address, city, zipcode, user) VALUES ('House', 5, 4, 2000, 2200, 435000, 495000, '11 Zurich Street', 'Bel Air', 10026, 10);

INSERT INTO offers (cust_id, property_id, bid, amtsold, decision) VALUES (1, 1, 25000, 30000, 0);
INSERT INTO offers (cust_id, property_id, bid, amtsold, decision) VALUES (2, 2, 33000, 39990, 0);
INSERT INTO offers (cust_id, property_id, bid, amtsold, decision) VALUES (3, 3, 35000, 45000, 1);
INSERT INTO offers (cust_id, property_id, bid, amtsold, decision) VALUES (4, 4, 30000, 60000, 0);
INSERT INTO offers (cust_id, property_id, bid, amtsold, decision) VALUES (5, 5, 12000, 23500, 0);
INSERT INTO offers (cust_id, property_id, bid, amtsold, decision) VALUES (6, 6, 70000, 88000, 1);
INSERT INTO offers (cust_id, property_id, bid, amtsold, decision) VALUES (7, 7, 300000, 335000, 1);
INSERT INTO offers (cust_id, property_id, bid, amtsold, decision) VALUES (8, 8, 90000, 120000, 0);
INSERT INTO offers (cust_id, property_id, bid, amtsold, decision) VALUES (9, 9, 40000, 50000, 1);
INSERT INTO offers (cust_id, property_id, bid, amtsold, decision) VALUES (10, 10, 350000, 495000, 0);
