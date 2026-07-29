





@router.post("/{ticket_id}/items")
def add_ticket_item(ticket_id: int, request: AddTicketItemRequest):
    ticket_found = None 
    

    for ticket in FAKE_TICKETS:
        if ticket["id"] == ticket_id:
            ticket_found = ticket
            break
        
    if ticket_found is None:
        raise HTTPException(status_code=http_status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    

    ticket_status = ticket_found["status"]


    if ticket_found["status"] != "open":
        raise HTTPException(status_code=http_status.HTTP_409_CONFLICT, detail=f"Cannot add items to a {ticket_status} ticket")
    
    menu_item_id = request.menu_item_id
    price_key = request.price_key
    quantity = request.quantity

    
    menu_item_found = None

    for menu_item in menu_data["items"]:
        if menu_item["id"] == menu_item_id:
            menu_item_found = menu_item
            break
    
    if menu_item_found is None:
        raise HTTPException(status_code=http_status.HTTP_404_NOT_FOUND, detail="Menu item not found")
    
    if not menu_item_found["inStock"]:
        raise HTTPException(status_code=http_status.HTTP_409_NOT_FOUND, detail="Menu item is out of stock!")


    return {
        "ticket": ticket_found,
        "menu_item": menu_item_found,
        "price_key": price_key,
        "quantity": quantity,
    } 


