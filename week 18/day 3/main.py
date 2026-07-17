#app/main.py 

from fastapi import FastAPI 

from app.dp import test_db_connection 


#what is test db connection ?

#this is a test function , to prove your fastapi app can talk to the postgresql 

# the small function looks like this 
def test_db_connection() -> int:
    with engine.connect() as connection:
         result = connection.execut(text("SELECT 1"))
         return result.scalar_one()








@app.get("/db-test")
def db_test():
     result = test_db_connection()

     return {
          "database": "connected",
          "result": result, 
     }



