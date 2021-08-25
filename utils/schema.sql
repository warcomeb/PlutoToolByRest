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
  Name varchar(100) NOT NULL,
  Description TEXT NOT NULL,
  CategoryId INTEGER NOT NULL
);

INSERT INTO subcategory (Id, Name, Description, CategoryId) VALUES (1,  'Undefined', '', 1);
