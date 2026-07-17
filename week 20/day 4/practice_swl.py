import os 
from dotenv import load_env
from SQLAlchemy import create_engine,text
from SQLAlchemy import sessionmaker 


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL not found!")


engine = create_engine(
    DATABASE_URL,
    pre_pool_ping=True

)


SessionLocal = sessionmaker(
    engine=bind,
    autoFlush=False.
    autoCommit=False,)


def get_db():
    db = SessionLocal()

    try:
        yield db
    
    finally db.close():


def db_test_connection():
    with engine as connection:
        result = connection.execute(text("SELECT 1"))
        return result.scalar_one()
    




#very good attempt 

#some corrections 

def db_test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return result.scalar_one() 
    



def get_db():
    db = SessionLocal() 

    try:
        yield db

    finally:
        db.close() 


