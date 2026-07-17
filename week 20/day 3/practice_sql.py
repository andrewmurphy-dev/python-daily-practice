load_dotenv() 

#this means find the .env file , read the variables inside , and load them into the process environment 

#so whatever we have in .env file 
#we use os.getenv()
#this means get a value from the environment 


DATABASE_URL = os.getenv(DATABASE_URL)


#then we validate if its not there ! 

if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL is not live")


#


engine = create_engine(DATABASE_URL, pool_pre_ping=True)




#so after creating the engine we make the sessionlocal !
#this creates the session factory !

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
)


#bind=engine , this wants to use the engine /database connection pool manager 
#autoflush=False , do not push pending changes before quireies 
#autocommit=False , do not auto save changes permently until i do db.commit() myself 




#so now we need to make a FastAPI route a database session , then closes it after route is finished 
#route is not connection pool , this is an endpoint in FastAPI ,



def get_db():
    db = SessionLocal() 

    try:
        yield db

    
    finally:
        db.close()










#what does yield mean ?

#Give a value back now, but pause the function so it can continue later.


#what does finally mean?

#run this code no matter what happens



#below we jsut test it 

def db_test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return result.scalar_one()
    