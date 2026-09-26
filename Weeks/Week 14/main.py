from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()


class createitem(BaseModel):
    name: str = Field(min_length=1)
    price: int = Field(gt=0)
    category: str = Field(min_length=1)




menu_items = [
    {
        "id": 1,
        "name": "Beer",
        "price": 700,
        "category": "drink",
        "is_active": True
    }
]




@app.get("/")
def home():
    return {"message": "Welcome to the menu API!"}



@app.get("/menu")
def get_menu_items():
    return menu_items




@app.get("/menu/{item_id}")
def get_menu_id(item_id: int):
    for menu_item in menu_items:
        if menu_item["id"] == item_id:
            return menu_item
        
    raise HTTPException(status_code=404, detail="Item not found")






@app.post("/menu")
def create_menu_item(item: createitem):
    new_item = {
        "id": len(menu_items) + 1,
        "name": item.name,
        "price": item.price,
        "category": item.category,
        "is_active": True
    }
    menu_items.append(new_item)
    return new_item




