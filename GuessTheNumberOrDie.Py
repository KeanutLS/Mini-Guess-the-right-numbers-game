import random
# I use the vs code terminal for this. No idea how it works elsewhere.

def PickWrongNumberISDie(players):
    
    print()
    max_player_count = 5 #not used but too lazy to remove
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
              
        available_numbers = [num for num in range(1, 21) if num not in chosen_numbers]

        if len(available_numbers) == 0:
            break

        if len(chosen_numbers) < len(players) - 1:
            dangerous_number = random.choice(available_numbers)
        else:
            dangerous_number = available_numbers[0]

        for player in players: #makes every non eliminated player available to choose a number with a list of all available numbers
            if player not in eliminated_players:
                print(player + " can now choose a number.")
                print("Available numbers:", available_numbers)

                chosen_number = int(input("Enter a number: "))

                while chosen_number < 1 or chosen_number > 20 or chosen_number in chosen_numbers: #checks if the player chooses a correct number, else it would display a message
                    if chosen_number < 1 or chosen_number > 20:
                        print("Invalid number! Please choose a number between 1 and 10.")
                    else:
                        print("Number already chosen! Please select another number.")

                    chosen_number = int(input("Enter a number: "))

                chosen_numbers.append(chosen_number)
                available_numbers.remove(chosen_number)  #remove chosen numbers when out of available numbers
                print(player + " chose:", chosen_number)
                print()

                if chosen_number == dangerous_number: #this is to detect of player is dead
                    print(player + " " + random.choice(death_messages))
                    eliminated_players.append(player)
                    chosen_numbers = []
                    available_numbers = [num for num in range(1, 21) if num not in chosen_numbers]  # reset available numbers so you can use them again if someone dies
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
print("Welcome to choose right or die. You will be able to choose a number, and if you choose the wrong number, you will die.")
print()
print("Input player names (press Enter to start the game):")
while True:
    player_name = input()
    if player_name == "":
        break
    player_list.append(player_name)
print()
PickWrongNumberISDie(player_list)

