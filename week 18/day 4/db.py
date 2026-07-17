import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker 


load_dotenv()

##what is os.getenv?

#to create an engine what do i need?


engine = create_engine( DATABASE_URL, pool_pre_ping=True, )

#what is happening here ?

#this makes a SQLAlchemy engine using our database 
#create_engine() , this creates the database connection control object ! 

#what is pool_pre_ping=True?
#this means before using an old/reused database connection check if its still alive ?
#its like an error and validation ! 
#the result is stoored in engine 
``

#to create session local what do i need ?

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


#day 5 
