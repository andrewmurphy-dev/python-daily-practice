--so going forward we need to save two files , the sql commands and the database
-- without running lets test ourselves yesterday 


CREATE TABLE users (
name TEXT PRIMARY KEY, 
id INTEGER NOT NULL,
age INTEGER NOT NULL
); 


-- you can have column definitions 
-- the general structure for making a column name is as follows 
-- column_name        data_type      consraints 9
-- we also need to insert a PRIMARY KEY 
--what is a primary key ?
--this is just a UNIQUE ID 
--







-- rememeber we close with semi-colon 
-- we dont use INT, we use INTEGER 
-- CREATE TABLE MAKES A TABALE 

--so how do we insert into this data ?

INSERT INTO users (name, id, age)
-- after this you need VALUES 
VALUES 
("andrew", 8282, 25).
("jack", 2929, 22); 

