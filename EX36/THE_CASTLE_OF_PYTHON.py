# -*- coding: utf-8 -*-
import time
from random import *
from sys import exit


# These are all the funtions for the start room:
def start_welcome():
    print """
                                                        !_
                                                    |*~=-.,
                                                    |_,-'`
                                                    |
                                                    |
                                                   /^
                     !_                           /   \\
                     |*`~-.,                     /,    \\
                     |.-~^`                     /#"     \\
                     |                        _/##_   _  \_
                _   _|  _   _   _            [ ]_[ ]_[ ]_[ ]
               [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|
             !_ |_=_ =-_-_  = =_|           !_ |=_= -    |
             |*`--,_- _        |            |*`~-.,= []  |
             |.-'|=     []     |   !_       |_.-"`_-     |
             |   |_=- -        |   |*`~-.,  |  |=_-      |
            /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  |
        _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      |
       [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    |
        |/#"     \_=-___=__=__- =-_ -=_ /#"     \| _ []  |
       _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\\
      [ ]_[ ]_[ ]_[ ]=_0~[_ _ _]~0   [ ]_[ ]_[ ]_[ ]=-   | \\
      |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \\
       | _- =-     |-_   | ((* |      |= _=       | -    |___\\
       |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\|
       | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
       |-_=- _     |=_   =            |=_= -_     |  =   ||+||
       |=_- /+\    | -=               |_=- /+\    |=_    |^^^|
       |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
       |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/
       |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/
       | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/
       |=_ =       | =_-_| |  | |     |   =_      | -_   |
       |_=-_       |=_=  | |  | |     |=_=        |=-    |
 `^^^^^^^^^^`^`^^`^`^`^^^""""""""^`^^``^^`^^`^^`^`^``^`^``^``^^

            WELCOME TO THE CASTLE OF PYTHON!
 """
    start_password()


def start_password():
    password = raw_input("\n\tType in the password: ")
    if password == "wise20162016":
        print "\n\tCorrect!"
        setup()
    else:
        print "\n\tPassword not correct. Hint: It's our tumblr password!"
        start_password()


def setup():
    key_found = "no"
    user_name = raw_input("\n\tType a username: ")
    print "\n\tWelcome to the castle, %s!" % user_name
    weapon_list = ['sword', 'shotgun', 'candy']
    weapon_string = ' or '.join(weapon_list)
    user_weapon = raw_input("\n\tChoose your weapon:\n \n\t{} >> ".format(weapon_string)).lower()
    if user_weapon in weapon_list:
        print "\n\tAlright, the %s will be your weapon!" % user_weapon
        time.sleep(1)
        print "..."
        time.sleep(1)
        print "..."
        time.sleep(1)
        print "..."
        time.sleep(1)
        start_room(user_name, user_weapon, key_found)
    else:
        print "\n\t%s?! Please concentrate a little more, in this castle we type everything exactly right! \n\tBy the way, what was your name again?" % user_weapon
        setup()

def start_room(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    print """
        %s, you find yourself in the castle's impressive entrance hall.
        Actually, it's not that impressive: All you can see is an old trunk and a door.
        Oh and of course you have your %s with you.
        So, what do you want to do?

        1. Check out the trunk

        2. Go through the door""" % (user_name, user_weapon)
    start_room_choice(user_name, user_weapon, key_found)


def start_room_choice(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    start_room_decision = raw_input("\n\t>> ").lower()
    # print "your name is %s your weapon is %s - the key is found? %s" % (user_name, user_weapon, key_found)
    if "1" in start_room_decision or "check" in start_room_decision or "trunk" in start_room_decision:
        if key_found == "no":
            print "\n\tThe trunk is locked."
            start_room(user_name, user_weapon, key_found)
        elif key_found == "yes":
            print "\n\tYou pick out Shaw's key and put it into the trunk's lock - it fits! \n\tThe trunk slowly opens up and..."
            end_win(user_name)
        else:
            end_wtf()
    elif "2" in start_room_decision or "go" in start_room_decision or "door" in start_room_decision:
        print "\n\tOk, let's get in there ..."
        jonathan_office(user_name, user_weapon, key_found)
    else:
        print "\n\tI'm afraid that's not an option!"
        start_room_choice(user_name, user_weapon, key_found)


# These are all the functions for Jonathan's room:
def jonathan_office(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    print "\n\tYou are in Jonathan Reus' office. What do you want to do? \n\n\t1. Talk to Jonathan \n\n\t2. Go through the door to your right \n\n\t3. Go back to start"
    jonathan_decision = raw_input("\n\t>> ").lower()
    if "1" in jonathan_decision or "jonathan" in jonathan_decision or "talk" in jonathan_decision:
        jonathan_talk(user_name, user_weapon, key_found)
    elif "2" in jonathan_decision or "door" in jonathan_decision or "right" in jonathan_decision:
        python_room(user_name, user_weapon, key_found)
    elif "3" in jonathan_decision or "start" in jonathan_decision or "back" in jonathan_decision:
        start_room(user_name, user_weapon, key_found)
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
        end_loose("\n\tWhat's wrong with you?! That was rude.\n")
    elif "2" in jonathan_reaction or "compliment" in jonathan_reaction:
        print "\n\t'Oh thank you %s, your hair also looks great today. Let me give you a hint: \n\n\tDon't enter the next room without having a shotgun!'" % user_name
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
            print "\n\tJonathan gave you a shotgun, this is your new weapon."
            jonathan_office(user_name, "shotgun", key_found)
        else:
            end_wtf()


# These are all the functions for the python's room:
def python_room(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    print """
    \tHOLY SHHHHHHHH...
               /^\/^)
         _|__|  O|
\/     /~     \_/ )
 \____|__________/  )
        \_______      )
                `\     \                 *
                  |     |                  )
                 /      /                    )
                /     /                       ))
              /      /                         \ )
             /     /                            \  )
           /     /             _----_            \   )
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~
    \n\tA GIANT PYTHON AWAITS YOU IN THIS ROOM."""
    python_choice(user_name, user_weapon, key_found)


def python_choice(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    print "\n\tWHAT ARE YOU GOING TO DO NOW?!"
    python_choices_list = ['run', 'fight', 'STOP SHOUTING']
    python_choices_string = ' or '.join(python_choices_list)
    python_decision = raw_input("\n\tThis is a lisssst, so type exactly one of the following:\n\n\t{} >> ".format(python_choices_string))
    if python_decision == python_choices_list[0]:
        print "\n\tToo late, that nasty python is blocking your way!"
        python_choice(user_name, user_weapon, key_found)
    elif python_decision == python_choices_list[1]:
        python_fight(user_name, user_weapon, key_found)
    elif python_decision == python_choices_list[2]:
        print "\n\tok ok i'm so sorry but still..."
        python_choice(user_name, user_weapon, key_found)
    else:
        end_loose("\n\tYou're obviously not capable of typing exactly what I told you to... \n\n\t...so the python will play with your dead body in a while-loop. #sorrynotsorry\n")


def python_fight(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    print "\n\tYou have to fight, there's no other way out. So you grab your %s and..." % user_weapon
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    if user_weapon == "sword":
        end_loose("\n\t...before you even get close to it the python eats you alive.\n")
    elif user_weapon == "shotgun":
        print """
        The snake starts shaking in fear. 'Pleasssse don't shhhhooot me!'

        Just in case you're wondering: This is a game. Of course the snake can speak.

        'I'm more than what you sssssee, not jussst your average python. My name isss...
        ...Zed Shhhaw. I'm the master of python. And if you let me live I will give you the most precious item!'"""
        python_win(user_name, user_weapon, key_found)
    elif user_weapon == "candy":
        end_loose("\n\tCandy?! Why did you think this would be an useful weapon?!\n")
    else:
        end_wtf()

def python_win(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    print "\n\tWhat are you going to do - will you let that sneaky snake live?"
    python_win_decision = raw_input("\n\t>> ").lower()
    if python_win_decision == "yes":
        print "\n\t'Thank you sssso much! Take thisss, you truly dessserve it...'"
        print "\n\tPython Zed Shaw gave you a key! Now get out of here, there's nothing more to see."
        time.sleep(1)
        print "..."
        time.sleep(1)
        print "..."
        time.sleep(1)
        print "..."
        time.sleep(1)
        start_room(user_name, user_weapon, "yes")
    elif python_win_decision == "no":
        end_loose("\n\tYou honestly would shoot the legendary Zed Shaw? Go see a therapist!\n")
    else:
        print "\n\tWe have no time to mess around! Type 'yes' or 'no'!"
        python_win(user_name, user_weapon, key_found)


# These are all the functions for the final screens:
def end_loose(reason):
    print reason,
    print "\n\n\tGAME OVER"
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    print """
        NOOB!

_____________$$$$$$$$$$$$$$$$$$$
___________$$$$$$$$$$$$$$$$$$$$$$$
________$$$$___$$$$$$$$$$$$$$$___$$$
______$$$$______$$$$$$$$$$$$______$$$$
____$$$$$________$$$$$$$$$$________$$$$
___$$$$$__________$$$$$$$$___________$$$$
__$$$$$____________$$$$$$____________$$$$$
_$$$$$$____________$$$$$$$____________$$$$ $
_$$$$$$___________$$$$$$$$$___________$$$$ $$
_$$$$$$$_________$$$_$$$_$$$_________$$$$$ $$
_$$$$$$$$______$$$$___$___$$$$______$$$$$$ $$
_$$$$$$$$$$$$$$$$$___$$$___$$$$$$$$$$$$$$$ $$
_$$$_$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$_o $$
_$$$__$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$__$ $$
__$$$__$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$__o$ $$
__'$$o__$$__$$'$$$$$$$$$$$$$$'$$__$$_____o $$
____$$o$____$$__'$$'$$'$$'__$$______$___o$ $
_____$$$o$__$____$$___$$___$$_____$$__o$
______'$$$$O$____$$____$$___$$ ____o$$$
_________'$$o$$___$$___$$___$$___o$$$
___________'$$$$o$o$o$o$o$o$o$o$$$$'
______________'$$$$$$$$$$$$$$$$$$$ """
    exit(0)


def end_wtf():
    print"""
    I have no idea what just happened. But as a good programmer I have to say:

    That was probably my fault...

 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || |     ____     | || |  _______     | || |  _______     | || |  ____  ____  | |
| |   /  ___  |  | || |   .'    `.   | || | |_   __ \    | || | |_   __ \    | || | |_  _||_  _| | |
| |  |  (__ \_|  | || |  /  .--.  \  | || |   | |__) |   | || |   | |__) |   | || |   \ \  / /   | |
| |   '.___`-.   | || |  | |    | |  | || |   |  __ /    | || |   |  __ /    | || |    \ \/ /    | |
| |  |`\____) |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |  \ \_  | || |    _|  |_    | |
| |  |_______.'  | || |   `.____.'   | || | |____| |___| | || | |____| |___| | || |   |______|   | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'

    Maybe you could just start from the beginning again...?"""
    exit(0)

def end_win(name):
    user_name = name
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    print "..."
    time.sleep(1)
    print"""
    You found the holy grail of Python!

             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`

    %s, you are truly a worthy student of Shaw.

  _____ ____   _  __ _____ ___   ___  ______ ____
 / ___// __ \ / |/ // ___// _ \ / _ |/_  __// __/
/ /__ / /_/ //    // (_ // , _// __ | / /  _\ )
\___/ \____//_/|_/ \___//_/|_|/_/ |_|/_/ /___/""" % user_name
    exit(0)


# and this is the code that will get the game started:
start_welcome()
