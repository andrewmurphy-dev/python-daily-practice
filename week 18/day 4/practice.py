#today we are first gonna do some practice 



@app.health("/db-test")
def db_test():
    result = test_db_connection()


    return {
        "database": "connected",
        "result": result 
    }




def test_db_connection() -> int:
    with result.connection() as connection:
        result.execite(text("SELECT 1"))
        return result.scalar_one()
    




