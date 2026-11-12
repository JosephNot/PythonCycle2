# THE LOST TEMPLE - BEGINNER 
print("=== THE LOST TEMPLE ===") 
name = input("What is your name, explorer? ") 
print(f"Welcome, {name}! You stand at the temple entrance.") 
 
print("\n1. Enter the dark corridor") 
print("2. Explore the courtyard") 
choice = input("Choose 1 or 2: ").strip()

def input_checker(user_input, numbers):
    numbers = str(numbers)
    if not user_input.isdigit:
        print("Not acceptable input")

    if not user_input in numbers:
        print("Not in range")

if choice == "1": 
    print("You enter the dark corridor.") 
    print("You foud a stone door")

    user_input = input("Open or leave door(1,2): ")
    input_checker(user_input, [1,2])

    if user_input == "1":
        print("The door leads to a trap of spikes")
        print("Flying at you")

    else:
        print("The path leads futher in...")
        print()
        print("You find a chest in a room...")
        user_input = input("Open or leave chest(1,2): ")
        input_checker(user_input, [1,2])
        if user_input == "1":
            print("You found a portal to mass amount of gold")
        else:
            print("The floor colapeses and you die")
    # TODO 1: Ask whether to open the stone door (yes/no). 
    # TODO 2: Display a different outcome for each answer. 

elif choice == "2": 
    print("You find an overgrown courtyard.") 
    print("Inside the courtyard there is a tower")
    
    user_input = input("Climb or leave(1,2): ")
    user_input = input_checker(user_input, [1,2])
    # TODO 3: Ask whether to climb the tower (yes/no). 
    # TODO 4: Display a different outcome for each answer.

    if user_input == "1":
        print("You have reached the top and can see everything")
        print()
        print("You see a trap door")
        user_input = input("Step or leave(1,2): ")
        user_input = input_checker(user_input, [1,2])
        if user_input == "1":
            print("You fell into a pit of death...")

        else:
            print("You stand there for the rest of time...")
    else:
        print("The tower stand tall...")

else: 
    print("That is not a valid route.") 

print("That is the end of the explorer journey")
print("Bye", name)
# TODO 5: Print a closing message for the player. 