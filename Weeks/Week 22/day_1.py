from tickets import tickets, orders


def pay_ticket(ticket_id):
    ticket_found = None

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket_found = ticket
            break

    if ticket_found is None:
        print("Ticket not found")
        return

    if ticket_found["status"] != open:
        print("Ticket cannot be paid!")
        return 

    if ticket_found["total"] <= 0:
        print("Ticket total must be greater than 0!")
        return 

    if ticket_found["status"] == "open":
        ticket_found["status"] = "paid"
        ticket_found["paid_at"] = current_unix_time()


    return Ticket_found


#so my logic 
#we find the ticket 
#see if the ticket id matches the ticket id in the parameter 
#we stop the function if: Ticket found is None, ticket_found["status"] != open , ticket_found["total"]
#we use the != open and use this area to change the status to paid , and paid_at to unix time 

    


    


#harder question 


def pay_order(order_id):
    ticket_found = None 

    for ticket in orders:
        if ticket["id"] == order_id:
            ticket_found = ticket
            break

    if ticket_found is None:
        print("Ticket is not found!")
        return 

    if ticket_found["status"] != "open":
        print("order cannot be payed!")
        return


    if ticket_found["items"] == []:
        print("order has no items!")
        return 


    if ticket_found["total"] <= 0:
        print("Invalid Total")
        return 


    for item in ticket_found["items"]:
        if item["quantity"] <= 0:
            print("invalid item quantity")
            return 


    ticket_found["status"] = "paid"
    ticket_found["paid_at"] = current_unix_time()

    return ticket_found

    





    



