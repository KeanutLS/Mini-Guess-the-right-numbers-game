import random

def PickWrongNumberISDie(players):
    print()
    max_player_count = 5
    eliminated_players = []
    chosen_numbers = []
    death_messages = [
        "you died, I'm deeply disappointed in you",
        "chose the wrong number and killed himself",
        "got gunned down",
        "flew in the twin towers",
        "didn't get the W",
        "has been chosen to go to hell",
        "committed suicide",
        "ate too much Thai food and died"
    ]

    while len(eliminated_players) < len(players):
        if len(chosen_numbers) == 20:
            break
              
        available_numbers = [num for num in range(1, 21) if num not in chosen_numbers] #creates a list of numbers that aren't chosen yet

        if len(available_numbers) == 0:
            break

        if len(chosen_numbers) < len(players) - 1: #checks that the amount of chosen numbers is is less than the player amount - 1 
            dangerous_number = random.choice(available_numbers)#since the last player doesn't have to guess a number
        else:
            dangerous_number = available_numbers[0]

        for player in players:   #makes every non eliminated player available to choose a number with a list of all available numbers
            if player not in eliminated_players:
                print(player + " can now choose a number.")
                print("Available numbers:", available_numbers)

                chosen_input = input("Enter a number: ")
                while chosen_input == "" or not chosen_input.isdigit():#checks if the player chooses a correct number and not a string, else it would display a message
                    print("Invalid input! Please enter a valid number between 1 and 20.")
                    chosen_input = input("Enter a number: ")

                chosen_number = int(chosen_input)

                while chosen_number < 1 or chosen_number > 20 or chosen_number in chosen_numbers:
                    if chosen_number < 1 or chosen_number > 20:
                        print("Invalid number! Please choose a number between 1 and 20.")
                    else:
                        print("Number already chosen! Please select another number.")

                    chosen_input = input("Enter a number: ")
                    while chosen_input == "" or not chosen_input.isdigit():
                        print("Invalid input! Please enter a valid number between 1 and 20.")
                        chosen_input = input("Enter a number: ")

                    chosen_number = int(chosen_input)

                chosen_numbers.append(chosen_number)
                available_numbers.remove(chosen_number)  #removes chosen numbers when chosen out of available numbers
                print(player + " chose:", chosen_number)
                print()

                if chosen_number == dangerous_number: #this is to detect if a player dies
                    print(player + " " + random.choice(death_messages)) 
                    eliminated_players.append(player)
                    chosen_numbers = []     # reset available numbers so you can use them again if someone dies
                    available_numbers = [num for num in range(1, 21) if num not in chosen_numbers]  
                    if len(eliminated_players) == len(players) - 1:
                        break

        if len(eliminated_players) == len(players) - 1:
            break

        print("--------------------")
         #checks if there is only 1 player left when other players dies

    remaining_players = [player for player in players if player not in eliminated_players]
    if len(remaining_players) == 1:
        print("The winner is:", remaining_players[0])
    else:
        print("No winner. All players died.")

        # makes the list of player names that you give

player_list = []
print()
print("Welcome to choose right or die. You will be able     to choose a number, and if you choose the wrong number, you will die.")
print()
print("Input player names (press Enter to start the game):")
while True:
    player_name = input()
    if player_name == "":
        break
    player_list.append(player_name)
print()
PickWrongNumberISDie(player_list)
