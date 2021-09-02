DROP TABLE IF EXISTS category;

CREATE TABLE category (
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  Name VARCHAR(100) NOT NULL,
  Description TEXT NOT NULL
);

INSERT INTO category (Id, Name, Description) VALUES (1,  'Undefined', '');
INSERT INTO category (Id, Name, Description) VALUES (2,  'Bills', '');
INSERT INTO category (Id, Name, Description) VALUES (3,  'Automobile', '');
INSERT INTO category (Id, Name, Description) VALUES (4,  'Entertainment', '');
INSERT INTO category (Id, Name, Description) VALUES (5,  'Education', '');
INSERT INTO category (Id, Name, Description) VALUES (6,  'Home Needs', '');
INSERT INTO category (Id, Name, Description) VALUES (7,  'Healthcare', '');
INSERT INTO category (Id, Name, Description) VALUES (8,  'Income', '');
INSERT INTO category (Id, Name, Description) VALUES (9,  'People', '');
INSERT INTO category (Id, Name, Description) VALUES (10, 'Travel', '');
INSERT INTO category (Id, Name, Description) VALUES (11, 'Fees', '');
INSERT INTO category (Id, Name, Description) VALUES (12, 'Miscellaneous', '');
INSERT INTO category (Id, Name, Description) VALUES (13, 'Transfer', '');

DROP TABLE IF EXISTS subcategory;

CREATE TABLE subcategory (
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  Name VARCHAR(100) NOT NULL,
  Description TEXT NOT NULL,
  CategoryId INTEGER NOT NULL
);

INSERT INTO subcategory (Id, Name, Description, CategoryId) VALUES (1,  'Undefined', '', 1);

DROP TABLE IF EXISTS payeetype;

CREATE TABLE payeetype (
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  Name VARCHAR(50) DEFAULT NULL,
  Description TEXT
);

INSERT INTO payeetype (Id, Name, Description) VALUES (1,  'Undefined', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (2,  'People', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (3,  'Bank', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (4,  'Bar', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (5,  'Shop', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (6,  'Resturant', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (7,  'Hospital', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (8,  'Doctor', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (9,  'Transport', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (10, 'Utilities', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (11, 'Mechanic', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (12, 'Camping/Hotel', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (13, 'Internet', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (14, 'Industry', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (15, 'ITC Company', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (16, 'Insurance', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (17, 'Pharmacy', '');
INSERT INTO payeetype (Id, Name, Description) VALUES (18, 'Firm', '');

DROP TABLE IF EXISTS payee;

CREATE TABLE payee (
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  Name VARCHAR(100) NOT NULL,
  PayeeTypeId INTEGER NOT NULL DEFAULT '0',
  Email VARCHAR(100) DEFAULT '-',
  Phone VARCHAR(15) DEFAULT '-',
  Address VARCHAR(70) DEFAULT '-',
  City VARCHAR(30) DEFAULT '-',
  District VARCHAR(2) DEFAULT '-',
  ZipCode VARCHAR(5) DEFAULT '-',
  Country VARCHAR(2) DEFAULT '-',
  VATID VARCHAR(20) DEFAULT '-',
  NIN VARCHAR(20) DEFAULT '-',
  Active INTEGER(1) DEFAULT '1',
  Note TEXT
);
