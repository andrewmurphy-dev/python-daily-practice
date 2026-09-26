from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field



app = FastAPI()

class correctmenuitem(BaseModel):
    name: str = Field(min_length=1)
    price: int =Field(gt=0)
    category: str = Field(min_length=1)


menu_items = []

@app.get("/")
def home():
    return {"message": "app is running"}



@app.get("/menu")
def menu():
    return menu_items


@app.post("/menu")
def create_menu_item(MenuItem: correctmenuitem):
    new_item = {
        "id": len(menu_items) + 1,
        "name": MenuItem.name,
        "price": MenuItem.price,
        "category": MenuItem.category
    }
    menu_items.append(new_item)
    return new_item



@app.get("/menu/{item_id}")
def get_menu_id(item_id: int):
    for item in menu_items:
        if item["id"] == item_id:
            return item
        
    raise HTTPException(status_code=404, detail="Item not found")



##create delete menu item id 


@app.delete("/menu/{item_id}")
def delete_menu_item(item_id: int):
    for item in menu_items:
        if item["id"] == item_id:
            menu_items.remove(item)
            return {"message": "Item deleted successfully"}
        
    raise HTTPException(status_code=404, detail="Item not found")





#remember in order to get a local host !
#we must do this ! 

#uvicorn name_of_module:app --reload 
#i realized you need this ! 
#in order to obtain a local host which makes sense i feel ! 
#router decorator 
#@app.get("/")












 

