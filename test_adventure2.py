# THE LOST TEMPLE - INTERMEDIATE 
rooms = { 
    "entrance": { 
        "description": "You are at the temple entrance.", 
        "exits": {"north": "hall"}, 
        "item": "key" 
    }, 
    "hall": { 
        "description": "Torches flicker along a long hall.", 
        "exits": {"south": "entrance", "east": "vault"}, 
        "item": "bronze key" 
    }, 
    "vault": { 
        "description": "A sealed chest stands in the vault.", 
        "exits": {"west": "hall"}, 
        "item": "treasure" 
    } 
} 
 
current_room = "entrance" 
inventory = [] 
running = True 
 
def show_room(): 
    room = rooms[current_room] 
    print("\n" + room["description"]) 
    print("Exits:", ", ".join(room["exits"])) 
    print("Item:", room["item"] or "none") 
 
while running: 
    show_room() 
    command = input("\nMove (direction), take, bag or quit: ").lower().strip() 
    if command == "quit": 
        running = False 
 
    elif command == "bag": 
        print("Inventory:", inventory) 
 
    elif command == "take": 
        room_items = rooms[current_room]["item"]
        rooms[current_room]["item"] = None
        print(room_items)
        if not room_items:
            inventory.append(room_items)

        
        # TODO 1: Check if the current room has an item. 
        # TODO 2: Add the item to inventory. 
        # TODO 3: Set the room item to None. 
        pass 

    
    elif command in rooms[current_room]["exits"]:
        next_room = rooms[current_room]["exits"][command]
        print("ff")
        print(next_room)
 
        # TODO 4: Require the bronze key before entering the vault. 
        # TODO 5: Otherwise change current_room to next_room. 
        pass 
 
    else: 
        print("Unknown command.") 
 
# TODO 6: Print a victory message if treasure was collected. 