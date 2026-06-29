import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine, text 
from sqlalchemy.osm import sessionmaker 






load_dotenv() 
#reads .env file , loads it into the environment 



#so we do this next!

DATAVASE_URL = os.getenv("DATABASE_URL")


#what is os in this state?

#os is a built in python module 

#it asks the operating system for the value DATABASE_URL 

os.getenv("DATABASE_URL") # --> gets the value 




#next is validtion of getting this value DATABASE_URL 

if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL is not set")

#next we need to create our engine ! 

engine - (
    DATEBASE_URL,
    pool_pre_ping=True
)

#DATABASE_URL = where the database is
#create_engine(...) = create the database connection manager
#engine = store that manager in a variable called engine



#pool
#pre
#ping
#=True 

#this means "before tusing a database connection check if its still alive ! "
#pooprepi

#next is sessionLocal 


SessionLocal = sessionmaker( bind=engine, autoflush=False, autocommit=False)

#what is this ?
#this is a session factory !
#it creates database sessions when ur api needs one!





#sessionmaker is a class 
#bind,autoflush, auto commit are arguments going into the class constructer 


#what is bind endgine?

#the engine knows ur database url , so Bind=engine connects the sessions to PostGreSQL

##autoflush 
#this means do not auto send pending changes to the database before it quires 

#what does flush mean ?

#send the pending SQL to PostgreSQL now , but do not permently sve it yet 


#what does auto commit mean ?

#do not permently save database changes automatically , i will call db.commit() 





#this is next ! 


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()




#this part gives your api route a temporary database session , then closes it after the request failed ! 


#what is yield ?

#this gives the database session to FastAPI 

#finally , this makes sure the database session gets closed !

#what does db = SessionLocal()

#create one active database session ! 

