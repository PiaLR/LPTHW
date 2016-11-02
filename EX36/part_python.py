import time

def python_room(name, weapon, key):
    user_name = name
    user_weapon = weapon
    key_found = key
    print """
    HOLY SHHHHHHHH...
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
        print "\n\tYou're obviously not capable of typing exactly what I told you to... \n\n\t...so the python will play with your dead body in a while-loop. #sorrynotsorry" #NOOB!# LOOSE SCREEN


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
        print "\n\t...before you even get close to it the python eats you alive."
        # LOOSE SCREEN
    elif user_weapon == "shotgun":
        print """
        The snake starts shaking in fear. 'Pleasssse don't shhhhooot me!'

        Just in case you're wondering: This is a game. Of course the snake can speak.

        'I'm more than what you sssssee, not jussst your average python. My name isss...
        ...Zed Shhhaw. I'm the master of python. And if you let me live I will give you the most precious item!'"""
        python_win(user_name, user_weapon, key_found)
    elif user_weapon == "candy":
        print "\n\tCandy?! Why did you think this would be an useful weapon?!"
        # LOOSE SCREEN
    else:
        print "\n\tWTF SCREEN" # wtf screen

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
        #start_room(user_name, user_weapon, "yes")
    elif python_win_decision == "no":
        print "LOOSE" # loose screen
    else:
        print "\n\tWe have no time to mess around! Type 'yes' or 'no'!"
        python_win(user_name, user_weapon, key_found)

python_room("test", "candy", "no")
