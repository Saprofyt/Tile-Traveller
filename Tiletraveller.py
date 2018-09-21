import sys
room_list = [] 

# Makes a list with our rooms and their directiona choices, Structure --> N,E,S,W 
room_list.append(["1,1, You can go North.",1,None,None,None])           #0
room_list.append(["1,2, You can go North, East or South.",2,4,0,None])  #1
room_list.append(["1,3, You can go East or South.",None,5,1,None])      #2
room_list.append(["2,1, You can go North.",4,None,None,None])           #3
room_list.append(["2,2, You can go South or West.",None,None,3,1])      #4
room_list.append(["2,3, You can go East or West.",None,8,2,None])       #5
room_list.append(["3,1, You can go North",7,None,None,None])            #6
room_list.append(["3,2, You can go North or South.",8,None,6,None])     #7
room_list.append(["3,3, You can go West or South.",None,None,7,5])      #8

# Defaults our room to the first one
current_room = 0


print(room_list)



# Foor our while-loop
done = False

# Dictionary with one char strings as keys and a number as value that correspondence a direction
directions = {"N":1,"E":2,"S":3,"W":4}

# Initialize the main loop of the game, it player inputs q the boolean will be set to true and exit the loop.
while not done:

    # Prints out the current_rooms list information and their directional choices
    print("\n"+room_list[current_room][0])

    # Initialize our question variable
    q = "0"

    # Boolean to check if user inputs valid directional choice
    valid_choice = False

    # Our questionaire loop, while user dosen't input valid choice this will loop
    while not valid_choice:

        # We use our dictionary to take the players input and use it as key to get our value.
        # Loops while we ain't getting a value from our dictionary, loop exist when we get a value that exist in our dictionary
        while not directions.get(q.title()): # .title() used to get be non case sensative.
           
            # If we get an unrecognized input we ask user to try again
            if q != "0":
                print("What direction is that?, Try again...")
            # Takes user input
            q = input("Where do you want to go? ( Quit (Q) )")
            # Check is user inputs Q, if that is the case we quit
            if q.title() == "Q":
                print("You pressed Q. Exit")
                sys.exit() # Forcefully quits the program.

        # Sets our next move tbe the value of our dictionary with user input key
        next_move = directions.get(q.title()) 

        # Gets our next room from the room list
        next_room = room_list[current_room][next_move]

        # If statement to check if the next_room exist and is a valid chice,
        if next_room:
            # Sets the boolean true that the user made a valid choice
            valid_choice = True
            current_room = next_room                
        else: # if a valid room dosen't exist we send a msg letting the user know and prints the current_rooms options again
            print("You can't go that way")
            print("\n"+room_list[current_room][0])
            q = "0" # reset question

    