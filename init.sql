-- create a table
CREATE TABLE countries(
  isocode2 varchar(2) PRIMARY KEY NOT NULL,
  isocode3 varchar(3) NOT NULL,
  countryname varchar(50) NOT NULL
);

-- add test data
INSERT INTO countries (isocode2, isocode3, countryname)
  VALUES ('ES', 'ESP', 'Spain'),
  ('UK', 'UKG', 'United Kingdom');