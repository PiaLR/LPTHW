from random import *

def jonathan_office(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    print "\n\tYou are in Jonathan Reus' office. What do you want to do? \n\n\t1. Talk to Jonathan \n\n\t2. Go through the door to your right \n\n\t3. Go back to start"
    jonathan_decision = raw_input("\n\t>> ").lower()
    if "1" in jonathan_decision or "jonathan" in jonathan_decision or "talk" in jonathan_decision:
        jonathan_talk(user_name, user_weapon, key_found)
    elif "2" in jonathan_decision or "door" in jonathan_decision or "right" in jonathan_decision:
        print "NEXT ROOM SCREEN" # python_room(name, weapon, key)
    elif "3" in jonathan_decision or "start" in jonathan_decision or "back" in jonathan_decision:
        print "STARTING ROOM" # start_room(name, weapon, key)
    else:
        print "\n\tI'm afraid that's not an option."
        jonathan_office(user_name, user_weapon, key_found)


def jonathan_talk(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    print "\n\t'Oh hey there, %s!', Jonathan says. How do you react? \n\n\t1. Insult him \n\n\t2. Compliment him \n\n\t3. Tell him you're bored" % user_name
    jonathan_reaction = raw_input("\n\t>> ").lower()
    if "1" in jonathan_reaction or "insult" in jonathan_reaction:
        print "rude! - LOOSE SCREEN" # LOOSE SCREEN
    elif "2" in jonathan_reaction or "compliment" in jonathan_reaction:
        print "\n\t'Oh thank you [USER_NAME], your hair also looks great today. Let me give you a hint: \n\n\tDon't enter the next room without having a shotgun!'"
        jonathan_office(user_name, user_weapon, key_found)
    elif "3" in jonathan_reaction or "bored" in jonathan_reaction:
        print "\n\t'Do you want to play a guessing game?', Jonathan asks excited."
        jonathan_game(user_name, user_weapon, key_found)
    else:
        print "\n\tI'm afraid that's not an option."
        jonathan_office(user_name, user_weapon, key_found)


def jonathan_game(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    guess_game = raw_input("\n\t>> ").lower()
    if guess_game == "yes":
        game_solution = randint(1, 20)
        print "\n\t'Alright %s, I just randomly picked a number between 1 and 20 - which one do you think it is?'" % user_name
        jonathan_guess(user_name, user_weapon, key_found, game_solution)
    elif guess_game == "no":
        print "\n\tJonathan is sad: 'You're missing out on something, %s!'" % user_name
        jonathan_office(user_name, user_weapon, key_found)
    else:
        print "\n\t'I can't understand you, pleas answer with yes or no.'"
        jonathan_game(user_name, user_weapon, key_found)


def jonathan_guess(name, weapon, key, solution):
    user_name = name
    user_weapon = weapon
    key_found = key
    game_solution = solution
    guess = raw_input("\n\t>> ")
    try:
        guess = int(guess)
    except ValueError:
        print "\n\t'You need to type in a valid integer number!'"
        jonathan_guess(user_name, user_weapon, key_found, game_solution)
    else:
        if guess > solution:
            print "\n\tJonathan shakes his head: 'No, my number is lower! Try again, %s.'" % user_name
            jonathan_guess(user_name, user_weapon, key_found, game_solution)
        elif guess < solution:
            print "\n\tJonathan shakes his head: 'No, my number is greater! Try again, %s.'" % user_name
            jonathan_guess(user_name, user_weapon, key_found, game_solution)
        elif guess == solution:
            print "\n\tJonathan smiles: 'That's exactly right, %d is the number I picked! Take this shotgun as a reward.'" % solution
            print "\n\tJonathan gave you a shotgun."
            jonathan_office(user_name, "shotgun", key_found)
        else:
            print "WTF SCREEN" # wtf screen






jonathan_office("Pia", "sword", "no")
