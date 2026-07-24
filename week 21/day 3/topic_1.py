#so here we are going to understand FAKE_TICKETS DATA 

FAKE_TICKETS = [
    {
        "id": 1,
        "name": "John",
        "status": "open",
        "items": [],
        "total": 0,
        "created_at": "2026-06-09T12:20:00Z",
        "paid_at": None,
    },
    {
        "id": 2,
        "name": "Sarah",
        "status": "paid",
        "items": [
            {
                "id": 1,
                "name": "Asahi Beer",
                "quantity": 2,
                "price": 800,
            },
            {
                "id": 2,
                "name": "Cover Charge",
                "quantity": 1,
                "price": 500,
            },
        ],
        "total": 2100,
        "created_at": "2026-06-09T12:30:00Z",
        "paid_at": "2026-06-09T13:10:00Z",
    },
    {
        "id": 3,
        "name": "Mike",
        "status": "paid",
        "items": [
            {
                "id": 1,
                "name": "Gin & Tonic",
                "quantity": 1,
                "price": 800,
            },
            {
                "id": 2,
                "name": "Lemon Sour",
                "quantity": 1,
                "price": 700,
            },
            {
                "id": 3,
                "name": "Cover Charge",
                "quantity": 1,
                "price": 500,
            },
        ],
        "total": 2000,
        "created_at": "2026-06-09T14:00:00Z",
        "paid_at": "2026-06-09T15:20:00Z",
    },
    {
        "id": 4,
        "name": "Emma",
        "status": "cancelled",
        "items": [
            {
                "id": 1,
                "name": "Red Bull",
                "quantity": 1,
                "price": 700,
            }
        ],
        "total": 700,
        "created_at": "2026-06-09T16:00:00Z",
        "paid_at": None,
    },
]





















#so what is this data ?



#FAKE_TICKETS
#┌──────────────────────────────┐
#│ Ticket dictionary: John      │
#├──────────────────────────────┤
#│ Ticket dictionary: Sarah     │
#├──────────────────────────────┤
#│ Ticket dictionary: Mike      │
#├──────────────────────────────┤
#│ Ticket dictionary: Emma      │
#└──────────────────────────────┘



#the outer structure is a list 

#for each valye inside the list is one ticket dictionary 

for ticket in FAKE_TICKETS:
    print(ticket)



#First loop  → John's entire dictionary
#Second loop → Sarah's entire dictionary
#Third loop  → Mike's entire dictionary
#Fourth loop → Emma's entire dictionary



#ticket["id"] this gets the id of the current ticket 



#questions 








#question 1 


#Using your FAKE_TICKETS data, write plain Python code that loops through every ticket and prints only each ticket’s ID.



FAKE_TICKETS = [
    {
        "id": 1,
        "name": "John",
        "status": "open",
        "items": [],
    },
    {
        "id": 2,
        "name": "Sarah",
        "status": "paid",
        "items": [...],
    },
]



for ticket in FAKE_TICKETS:
    print(ticket["id"])



#First loop:
#ticket = John's dictionary
#ticket["id"] = 1

#Second loop:
#ticket = Sarah's dictionary
#ticket["id"] = 2



#question 2 


for ticket in FAKE_TICKETS:
    print(ticket["name"])


#John
#Sarah




#question 3 

for ticket in FAKE_TICKETS:
    print(ticket["status"])


#we needed both the name and the status 


for ticket in FAKE_TICKETS:
    print(ticket["name"], "-", ticket["status"])



#dont forget the comma


#John - open
#Sarah - paid



#question 4 


for ticket in FAKE_TICKETS:
    if ticket["id"] == 2:
        print(ticket)


#{'id': 2, 'name': 'Sarah', 'status': 'paid', 'items': [Ellipsis]}



#question 5 


ticket_id = 3

for ticket in FAKE_TICKETS:
    if ticket["id"] == ticket_id:
        print(ticket)




#question 6 


ticket_id = 2
found_ticket = None


for ticket in FAKE_TICKETS:
    if ticket["id"] == ticket_id:
        found_ticket = ticket
        print(found_ticket)


#Store the current matching ticket dictionary inside found_ticket.



ticket_id = 99
found_ticket = None


for ticket in FAKE_TICKETS:
    if ticket["id"] == ticket_id:
        found_ticket = ticket
        
    print(found_ticket)


#question 7 


ticket_id = 4
found_ticket = None


for ticket in FAKE_TICKETS:
    if ticket["id"] == ticket_id:
        found_ticket = ticket

if found_ticket is not None:
    print(found_ticket["name"])

else:
    print("Ticket not found!")


#question 8 


ticket_id = 3
found_ticket = None 

for ticket in FAKE_TICKETS:
    if ticket["id"] == ticket_id:
        found_ticket = ticket

if found_ticket is not None:
    print(found_ticket["name"], "-", found_ticket["status"], "-", found_ticket["total"])

else:
    print("Ticket not found!")




